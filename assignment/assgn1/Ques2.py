# =============================================================================
# a. You have to implement the decision tree algorithm for predicting whether a
# person defaulted or not based on various personal and economic attributes.
# Plot the train, validation and test set accuracies against the number of nodes 
# in the tree as you grow the tree. 
# On X-axis you should plot the number of nodes in the tree and Y-axis should represent the accuracy. Comment on your observations.
# =============================================================================

# Load the datasets
import pandas as pd

df_train = pd.read_csv('F:\\aindra\\Assignment 3\\credit-cards.train.csv')
df_test = pd.read_csv('F:\\aindra\\Assignment 3\\credit-cards.test.csv')
df_val = pd.read_csv('F:\\aindra\\Assignment 3\\credit-cards.val.csv')

datasets = [df_train, df_test, df_val]

for df in datasets:
    #print(df.head(2))
    df = df.iloc[1:]
    #df.drop()
    print(df.shape)      
    print(df.columns)      

X_train = df_train.iloc[1:, :-1]
X_test = df_test.iloc[1:, :-1]
X_val = df_val.iloc[1:, :-1]
y_train = df_train.iloc[1:, -1:]
y_test = df_test.iloc[1:, -1:]
y_val = df_val.iloc[1:, -1:]

datasets = [y_train, y_test, y_val ]
for df in datasets:
    print(df['Y'].unique())

datasets = [X_train, X_test, X_val]


from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier(max_depth = 2, random_state = 0)
clf.fit(X_train, y_train)

# Predict for 1 observation
clf.predict(X_test.iloc[0].values.reshape(1, -1))
# Predict for multiple observations
clf.predict(X_test[0:10])

score = clf.score(X_test, y_test)
print(score)



# List of values to try for max_depth:
max_depth_range = list(range(1, 10))
# List to store the average RMSE for each value of max_depth:

accuracy_train = []
accuracy_test = []
accuracy_val = []

for depth in max_depth_range:    
    clf = DecisionTreeClassifier(max_depth = depth, random_state = 0)
    clf.fit(X_train, y_train)
    score_train = clf.score(X_train, y_train)
    score_test = clf.score(X_test, y_test)
    score_val = clf.score(X_val, y_val)
    accuracy_train.append(score_train)
    accuracy_test.append(score_test)
    accuracy_val.append(score_val)
    
# Plot the scores
def plot_accuracies(accuracy_train, accuracy_test, accuracy_val):
    df = pd.DataFrame(list(zip(accuracy_train, accuracy_test, accuracy_val)), columns =['train', 'test', 'val'])
    df.plot.line(subplots=True)

plot_accuracies(accuracy_train, accuracy_test, accuracy_val)

# =============================================================================
# looking at the graph:
#     with increase in depth 
#     the accuracy increases on the training dataset => overfitting
#     on the test dataset, the accuracy increases by 1% @depth of 2, then starts decreasing
#     on the validation dataset, the accuracy increases slightly (in decimals) and then decreases
# take depth=2 as the optimal depth which gives best accuracy as 81.1%
# =============================================================================

# Let's run cross validation of the model
from sklearn.model_selection import cross_validate
depth = 2
clf = DecisionTreeClassifier(max_depth = depth, random_state = 0)
cv_results = cross_validate(clf, X_val, y_val, cv=5)
#sorted(cv_results.keys())
cv_results['test_score']
(cv_results['test_score']).mean()


# get confusion matrix for the best depth
from sklearn.metrics import classification_report, confusion_matrix
clf = DecisionTreeClassifier(max_depth = depth, random_state = 0)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test) #chk clf
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))




# =============================================================================
# b. Learn a Random Forest algorithm for the same dataset and report the findings
# as described above.
# c. Which attribute had the most impact for classification into defaulter or not
# according to the dataset?
# =============================================================================

# This requires looking into the features

df_train.describe().columns

import matplotlib.pyplot as plt
import seaborn as sns
fig=plt.subplots(figsize=(20,20))
for i, j in enumerate(X_train.columns):
    plt.subplot(5, 5, i+1)
    plt.subplots_adjust(hspace = 1.0)
    sns.countplot(x=j, data=df_train, hue='Y') 
    plt.xticks(rotation=90)
    plt.title("0: Engaged, 2: Unengaged")



# Import the model we are using
from sklearn.ensemble import RandomForestClassifier# Instantiate model with 1000 decision trees
from sklearn import metrics
estimators_range = list(range(10, 100, 10))
accuracy_rf = []

accuracy_train = []
accuracy_test = []
accuracy_val = []

for est in estimators_range:
    rf = RandomForestClassifier(n_estimators=est, random_state=42)
    rf.fit(X_train, y_train.values.ravel())
    score_train = rf.score(X_train, y_train)
    score_test = rf.score(X_test, y_test)
    score_val = rf.score(X_val, y_val)
    accuracy_train.append(score_train)
    accuracy_test.append(score_test)
    accuracy_val.append(score_val)


# getting best num estimators
# Plot the scores
def plot_accuracies(accuracy_train, accuracy_test, accuracy_val):
    df = pd.DataFrame(list(zip(accuracy_train, accuracy_test, accuracy_val)), columns =['train', 'test', 'val'])
    df.plot.line(subplots=True)

plot_accuracies(accuracy_train, accuracy_test, accuracy_val)

y_pred = rf.predict(X_test) #chk clf
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))


feature_imp = pd.Series(rf.feature_importances_,index=X_train.columns).sort_values(ascending=False)
feature_imp


https://www.datacamp.com/community/tutorials/random-forests-classifier-python