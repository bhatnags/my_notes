# =============================================================================
# STEP 1 GET AND CLEAN DATA
# =============================================================================

import numpy as np
import pandas as pd
import re
from pprint import pprint

url_data = 'https://raw.githubusercontent.com/selva86/datasets/master/newsgroups.json'

def read_data(url_data):
    df = pd.read_json(url_data)
    return df

def clean_data(df):
    # Convert to list
    data = df.content.values.tolist()
    # Remove Emails
    data = [re.sub('\S*@\S*\s?', '', sent) for sent in data]
    # Remove new line characters
    data = [re.sub('\s+', ' ', sent) for sent in data]
    # Remove distracting single quotes
    data = [re.sub("\'", "", sent) for sent in data]
    return data

df = read_data(url_data)
data = clean_data(df)
pprint(data[0])

# =============================================================================
# STEP 2 Tokenisation
# =============================================================================
# Gensim for Tokenisation
import gensim
from gensim.utils import simple_preprocess

def sent_to_words(sentences):
    for sentence in sentences:
        yield(gensim.utils.simple_preprocess(str(sentence), deacc=True))  # deacc=True removes punctuations
tokenized_data = list(sent_to_words(data))
print(tokenized_data[:1])


# =============================================================================
# STEP 3 REMOVE STOPWORDS
# =============================================================================

# Prepare Stopwords
import nltk
def get_stopwords():
    nltk.download('stopwords')
    from nltk.corpus import stopwords
    stop_words = stopwords.words('english')
    stop_words.extend(['from', 'subject', 're', 'edu', 'use'])
    return stop_words

stop_words = get_stopwords()

# Remove stopwords
def remove_stopwords(texts):
    return [[word for word in simple_preprocess(str(doc)) if word not in stop_words] for doc in texts]

# Remove Stop Words
tokenized_data_nostops = remove_stopwords(tokenized_data)


# =============================================================================
# STEP 4  Make bigrams, trigrams, quadgrams models
# =============================================================================

def get_bigram_model(tokenized_data):
    bigram = gensim.models.Phrases(tokenized_data, min_count=5, threshold=100) # higher threshold fewer phrases.
    bigram_mod = gensim.models.phrases.Phraser(bigram)
    return bigram_mod, bigram

def get_trigram_model(tokenized_data, bigram, bigram_mod):
    trigram = gensim.models.Phrases(bigram[tokenized_data], threshold=100)  
    trigram_mod = gensim.models.phrases.Phraser(trigram)
    print(trigram_mod[bigram_mod[tokenized_data[0]]])
    return trigram_mod, trigram

def make_bigrams(texts):
    return [bigram_mod[doc] for doc in texts]

def make_trigrams(texts):
    return [trigram_mod[bigram_mod[doc]] for doc in texts]

# Make bigram model
bigram_mod, bigram = get_bigram_model(tokenized_data)
# Form Bigrams
tokenized_data_bigrams = make_bigrams(tokenized_data_nostops)


# =============================================================================
# STEP 5 Lemmatization
# =============================================================================

# spacy for lemmatization
import spacy
# Initialize spacy 'en' model, keeping only tagger component (for efficiency)
nlp = spacy.load('en', disable=['parser', 'ner'])
# Lemmatization: keep only noun, adj, vb, adv
def lemmatization(texts, allowed_postags=['NOUN', 'ADJ', 'VERB', 'ADV']):
    texts_out = []
    for sent in texts:
        doc = nlp(" ".join(sent)) 
        texts_out.append([token.lemma_ for token in doc if token.pos_ in allowed_postags])
    return texts_out
data_lemmatized = lemmatization(tokenized_data_bigrams, allowed_postags=['NOUN', 'ADJ', 'VERB', 'ADV'])
print(data_lemmatized[:1])



# =============================================================================
# TOPIC MODELLING
# =============================================================================

# =============================================================================
# STEP 6: GET INPUTS FOR LDA
# =============================================================================

def lda_inputs():

    # Create inputs to the LDA topic model: 
    #  - dictionary(id2word) and 
    #  - the corpus
    
    # Gensim for LDA input
    import gensim.corpora as corpora
    id2word = corpora.Dictionary(data_lemmatized) # what word a given id corresponds to

    # Create Corpus
    texts = data_lemmatized
    corpus = [id2word.doc2bow(text) for text in texts] # Term Document Frequency is mapping of (word_id, word_frequency)

    return id2word, corpus

id2word, corpus = lda_inputs()

def print_corpus(id2word, corpus):
    print([[(id2word[id], freq) for id, freq in cp] for cp in corpus[:1]])


# =============================================================================
# STEP 7 Build LDA model
# =============================================================================

# for getting coherence score
from gensim.models import CoherenceModel

def lda_model(num_topics):

    model_list = []
    perplexity_value_list = []
    coherence_value_list = []

    for num in num_topics:
        lda_model = gensim.models.ldamodel.LdaModel(corpus=corpus,
                                                   id2word=id2word,
                                                   num_topics=num, 
                                                   random_state=100,
                                                   update_every=1, #how often the model parameters should be updated
                                                   chunksize=100, # number of documents to be used in each training chunk
                                                   passes=10, #total number of training passes
                                                   alpha='auto', # hyperparameters that affect sparsity of the topics (In Gensim: both defaults to 1.0/num_topics prior)
                                                   per_word_topics=True)

        # Compute Model Perplexity and Coherence Score =>  measure of how good a given topic model is
        # Compute Perplexity
        perplexity_lda = lda_model.log_perplexity(corpus)
        print('\nFor %d num of topics Perplexity: %f' % (num, perplexity_lda))  # a measure of how good the model is. lower the better.

        # Compute Coherence Score
        coherence_model_lda = CoherenceModel(model=lda_model, texts=data_lemmatized, dictionary=id2word, coherence='c_v')
        coherence_lda = coherence_model_lda.get_coherence()
        print('\nFor %d num of topics Coherence Score: %f' % (num, coherence_lda))
        
        model_list.append(lda_model)
        perplexity_value_list.append(perplexity_lda)
        coherence_value_list.append(coherence_lda)
        # a coherence score of 0.48 # higher is better # https://rare-technologies.com/what-is-topic-coherence/
    
    return model_list, perplexity_value_list, coherence_value_list

# num different topics where each topic is a combination of keywords and each keyword contributes a certain weightage to the topic
num_topics = list(range(1,5))
model_list, perplexity_value_list, coherence_value_list = lda_model(num_topics)

# Get num of topics for the best coherence value

import matplotlib.pyplot as plt
# %matplotlib inline
plt.plot(num_topics, coherence_value_list)
plt.xlabel("Num Topics")
plt.ylabel("Coherence score")
plt.legend(("coherence_values"), loc='best')
plt.show()



# Select the best model and print the topics
def best_model_topics(best_model):
    # =============================================================================
    #     returns a list of tuples
    #     first element of the tuple is the topic (or topic ID) and second element is the top 10 words that contribute to that topic
    #     0 gives the top 10 keywords that contribute to "Topic 0"
    #     The weights reflect how important a keyword is to that topic.
    #     looking at these words, one can summarze the topic
    #     
    #     doc_lda = lda_model[corpus]
    #     
    # =============================================================================
    #model_topics = best_model.show_topics(formatted=False)
    #pprint(best_model.print_topics(num_words=10))
    pprint(best_model.print_topics(num_words = 10))
    
best_model = model_list[3]
best_model_topics(best_model)



# =============================================================================
# # Visualize the topics-keywords
# # Plotting tools
# import pyLDAvis
# import pyLDAvis.gensim  # don't skip this
# 
# # Enable logging for gensim - optional
# import logging
# logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.ERROR)
# 
# import warnings
# warnings.filterwarnings("ignore",category=DeprecationWarning)
# 
# pyLDAvis.enable_notebook()
# vis = pyLDAvis.gensim.prepare(lda_model, corpus, id2word)
# vis
# =============================================================================



# Conclusions:
# maybe check Mallet first (https://www.machinelearningplus.com/nlp/topic-modeling-gensim-python/)
# 1 Finding the dominant topic in each sentence
# 2 Find the most representative document for each topic
# 3 Topic distribution across documents


# 1 Finding the dominant topic in each sentence
def format_topics_sentences(ldamodel=lda_model, corpus=corpus, texts=data):
    # Init output
    sent_topics_df = pd.DataFrame()

    # Get main topic in each document
    for i, row in enumerate(best_model[corpus]):
        row = sorted(row, key=lambda x: (x[1]), reverse=True)
        # Get the Dominant topic, Perc Contribution and Keywords for each document
        for j, (topic_num, prop_topic) in enumerate(row):
            if j == 0:  # => dominant topic
                wp = ldamodel.show_topic(topic_num)
                topic_keywords = ", ".join([word for word, prop in wp])
                sent_topics_df = sent_topics_df.append(pd.Series([int(topic_num), round(prop_topic,4), topic_keywords]), ignore_index=True)
            else:
                break
    sent_topics_df.columns = ['Dominant_Topic', 'Perc_Contribution', 'Topic_Keywords']

    # Add original text to the end of the output
    contents = pd.Series(texts)
    sent_topics_df = pd.concat([sent_topics_df, contents], axis=1)
    return(sent_topics_df)

df_topic_sents_keywords = format_topics_sentences(ldamodel=best_model, corpus=corpus, texts=data)

# Format
df_dominant_topic = df_topic_sents_keywords.reset_index()
df_dominant_topic.columns = ['Document_No', 'Dominant_Topic', 'Topic_Perc_Contrib', 'Keywords', 'Text']

# Show
df_dominant_topic.head(10)

# 2 Find the most representative document for each topic
# Group top 5 sentences under each topic
sent_topics_sorteddf_mallet = pd.DataFrame()

sent_topics_outdf_grpd = df_topic_sents_keywords.groupby('Dominant_Topic')

for i, grp in sent_topics_outdf_grpd:
    sent_topics_sorteddf_mallet = pd.concat([sent_topics_sorteddf_mallet, 
                                             grp.sort_values(['Perc_Contribution'], ascending=[0]).head(1)], 
                                            axis=0)

# Reset Index    
sent_topics_sorteddf_mallet.reset_index(drop=True, inplace=True)

# Format
sent_topics_sorteddf_mallet.columns = ['Topic_Num', "Topic_Perc_Contrib", "Keywords", "Text"]

# Show
sent_topics_sorteddf_mallet.head()



# 3 Topic distribution across documents
# Number of Documents for Each Topic
topic_counts = df_topic_sents_keywords['Dominant_Topic'].value_counts()

# Percentage of Documents for Each Topic
topic_contribution = round(topic_counts/topic_counts.sum(), 4)

# Topic Number and Keywords
topic_num_keywords = df_topic_sents_keywords[['Dominant_Topic', 'Topic_Keywords']]

# Concatenate Column wise
df_dominant_topics = pd.concat([topic_num_keywords, topic_counts, topic_contribution], axis=1)

# Change Column names
df_dominant_topics.columns = ['Dominant_Topic', 'Topic_Keywords', 'Num_Documents', 'Perc_Documents']

# Show
df_dominant_topics