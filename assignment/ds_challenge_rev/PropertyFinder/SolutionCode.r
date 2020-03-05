# Descriptive Statistics

# Data Mining in R




# First I create 3 csv files of the dataset

# Load the datasets in R

leads <- read.csv("F://JOBS//PropertyFinder//leads.csv", header = TRUE)
pageviews <- read.csv("F://JOBS//PropertyFinder//pageviews.csv", header = TRUE)
searches <- read.csv("F://JOBS//PropertyFinder//searches.csv", header = TRUE)


# Check the data is uploaded correctly
# Checked the number of observations and variables






summary(pageviews)
# The count of user_id and session_id is same, hinting that the user did all the searches in various sites and all that is recorded as one session


summary(searches)
# 5-6 repeated users with same session ID bifurcating at event ID, timestamp etc level
# 3 types of categories: buy (28%), rent(69%), rent_commercial(3%)
# property_type_id has 27NAs,and remaining values with mostly "1" value
# Min price column in this data ise useless with all NAs
#     => Or we can say people don't care about min price
# Max price is 2100000
#     => This value exceeds the value given on PropertyFinder.ae webpage (1,000,000 AED per year)
#     => So, I am not sure how this entered the database
# Min and max bedrooms have 78%-92% NAs respectively and remaining values with 1 
#     => most searches didn't care about number of bedrooms, otherwise requested for 1 bedroom, so by default it should be kept one to make the webpage more user friendsly
# Min and Max area both have NA values rendering them useless at this analysis level
# Furnishings is "NA", which means people don't care about whether the property is furnished/unfurnished
# But price period is telling that majority(72%) looks for yearly bookings, that means these users have assumed/know that the property will come furnished/unfurnished
# Looking at the "keywords" column, it can be inferred that 
#     => the keywords coming in majority can be displayed on the webpage to make it more friendly
#     => these keywords along with furnishings column can be clubbed together



summary(leads)
# event_name
#     => lead_click:lead_Send :: 91:9
# medium
#     => email(18%), phone(79%) & sms(3%)
# bedrooms, median is 1 and for bathrooms, median is 2
#     => while most of the people look for 1 bedroom apartment, the number of bathroom searches is 2
#     => the above point concludes to the sampling method used, which shows it is not stratified sampled
# the mean price of the leads is 266,328 and tried for booking it at yearly level (73%)
# most of the leads are for rent(73%), as leads for buy is only (27%)
# from this data it can be concluded that preference is for unfurnished apartments (85%), 
#     => as majority of the leads that are being captured are for unfurnished, with furnished adn part_furnished apartments are 9% and 7% respectively
# mostly leads are for residential area(87%), the remaining are leads for commerical properties
# Almost half of these leads are for standard property (52%), the remaining are covered by featured(34%) and premium (14%)
# Only 22% of these leads are verified
# The quality score of these sampled leads lie in 78.23%-98.92%  (Interquartile range)
# The data has been sampled on November 21st, 2018 




##################~~~~~~~~~~~~~~~~ Creating Factor Map ~~~~~~~~~~~~~~~~~~~~~~~~#############
# Writing down the relevant factors that can help in segmentation from each dataset

# pageviews
names(pageviews)
# user_id + session_id can be used for joining the tables
# Factors = page_url
unique(pageviews$page_url)
# This gives me 50+ uniques search URLs, implying that "page_url" will not be a good segmentation variable


# searches
names(searches)
# by looking at the results, it can be assumed that 
# domain_userid + domain_Sessionid + event_id would work as the primary key for joining the table
# Factors = category and price_period are important factors


# leads
names(leads)
# This clearly seemed an important dataset
# user_id + session_id can be used for joining the tables
# Factors = event_name, medium, bedrooms, bathrooms, price, price_period, offering_type, 
#           property_type_id,  furnishings, market, listing_status
# Since the price_period variable has only one value i.e. "yearly"
#       which when filled with any criteria (say "fill NAs with median") will result in whole column with one value
#       this will not help in segmentation, so the column is disregarded

# From searches to leads
# User IDs that became leads


library(dplyr)
searches <- rename(searches, user_id = domain_userid, session_id= domain_sessionid)
leads <- rename(leads, session_id=sessions_id)
names(searches)
names(leads)

unique(searches$user_id)
# Results in 10 User IDs
unique(leads$user_id)
# Results in 52 User IDs

intersect(searches$user_id , leads$user_id)
# Only two user IDs found which were converted from searches to leads

# Understanding these User IDs
# Filtering the data for the converted User IDs


summary(searches[(searches$user_id %in% leads$user_id),])
# Both of these leads are in buy category and the price period is Null

summary(searches[(leads$user_id %in% searches$user_id),])
# while the searches were for "buy" category, they turned out to be in "rent" lead

# data <- merge(searches, leads, 
#              by = c("user_id", "session_id", "timestamp"), 
#              all = TRUE)



# Preparing the dataset
vars <- c("user_id", "session_id", "timestamp", "event_name", "medium", "bedrooms", "bathrooms","price", "offering_type", 
          "property_type_id",  "furnishings", "market", "listing_status")
data <- leads[vars]
rm(vars)

summary(data)
# The resulted dataset has no null values, is clean & ready for modelling

# Export the data
write.csv(data, "F://JOBS//PropertyFinder//data.csv")




# RFM analysis
# Recency-Frequency-Monetary Analysis


# Recency - How recently did the user/lead visited the site?
# Frequency - How often do they visit?
# Monetary Value - How much worth of property are they planning to buy/rent?


rfm_data <- data[, c("user_id", "timestamp", "price")]

# For recency
rfm_data$recency <- Sys.time() - as.POSIXct(rfm_data$timestamp)
rfm_data$recency <- as.numeric(rfm_data$recency)

# For frequency
freq <-  aggregate(timestamp ~ user_id, rfm_data, function(x) length(unique(x)))
freq <- rename(freq, frequency = timestamp)
rfm_data <- merge(freq, rfm_data, by = "user_id", all.y = TRUE)
rm(freq)


# For monetary
rfm_data <- rename(rfm_data, monetary = price)
rfm_data <- rfm_data[-3]


# RFM summary
summary(rfm_data)

plot(rfm_data[2:4])
#Plot saved as RFM.png
# It can be seen that most users fall in medium to high recency and low monetary values
cor(rfm_data[2:4])




# Since the user IDs are repeatitive for frequency
unique_rfm <- unique(rfm_data[, c("user_id", "frequency")])

summary(unique_rfm)
# The quartile ranges of frequency has changed, 
#     => median changed from 2 to 1 and 3rd quartile changed from 5 to 2


# To further understand the same

def.par <- par(no.readonly = TRUE)
par(oma = c(0,0,3,0))
par(mfcol=c(3,1))

hist(rfm_data$recency, main = "Histogam of User recency rate on webpage",xlab = "User Recency (days difference from today)")

options(scipen = 10)
hist(rfm_data$monetary, main = "Histogam of User's search - monetary value", xlab = "User Monetary Value")

hist(unique_rfm$frequency, main = "User Frequency of searching the webpage", xlab = "User Frequency")


# removing the variables
rm(def.par)











# Clustering the dataset

# Since we have mixture mode, PCA is not a good way for variable reduction

# Variable reduction
# Before that we need to standardize the variables
# All numerical variables should be standardize with a mean of 0 and standard deviation of 1
range01 <- function(x){(x-min(x))/(max(x)-min(x))}

data$s_bedrooms <- range01(data$bedrooms)
data$s_bathrooms <- range01(data$bathrooms)
data$s_price <- range01(data$price)
# The rest of the variables are to be treated categorically


clust_data <- data[, c(4:5, 9:17)]

# Get the correlation between various variables
library(polycor)
# polycor library gives the correlation of the variables when the dataset consist of different datatypes
# Pearson correlation: correlation between two numerical variables
# Polychoric correlation: correlation between two categorical variables
# Polyserial correlation: correlation between a numerical and a categorical variable


hetcor(clust_data)
# From this we can conclude
# event_name & furnishings have high (Polychoric) correlation of 0.8834
#     The two variables can be clubbed
#     Since there won't be any standardization involved, one of these could be disregarded (furnishings)

# bedrooms, bathrooms, market
#     bedrooms & bathrooms have high (Pearson) correlation of 0.8871
#     bedrooms & market have high (Polyserial) correlation of 0.9748
#     bathrooms & market have high correlation of 0.8262
#     The three variables can be clubbed into one

# price has a high negative correlation with offering_type (-0.8172) and a high positive correlation with market (0.6049)
#     price can be clubbes with offering_type
#     price can be clubbed with market
#     thus reducing the 3 variables into 2 clubbed variables

# Convert categorical data to market numeric data
#clust_data$n_market <- unclass(clust_data$market) 
#clust_data$n_event_name <- unclass(clust_data$event_name)
#clust_data$n_furnishings <- unclass(clust_data$furnishings)


lm(clust_data$market ~ clust_data$s_bathrooms+clust_data$s_bedrooms)
# "Market" variable doesn't relate well with bathrooms & bedrooms
lm(clust_data$s_bedrooms ~ clust_data$s_bathrooms)

clust_data$apartment_size <- clust_data$s_bathrooms+clust_data$s_bedrooms


lm(clust_data$market ~ clust_data$offering_type)
# Not an interesting relationship => disregarded

lm(clust_data$market ~ clust_data$s_price )
# market = 1.8463 + 0.3939 * price
# disregarded

clust_data <- clust_data[, -c(9:10)]

library(clustMixType)

# Testing with multiple cluster groups (group size 2 to 10)
for (i in 2:9)
  kpres[[i]] <- kproto(clust_data, i)
summary(kpres[[2]])
clprofiles(kpres[[2]], clust_data)

# The two clusters seemed to have performed well on two variables: property_type_id & apartment_size bifurcation, 
#     in rest of the variables, the differences are not visisble

clprofiles(kpres[[9]], clust_data)
# looking at the 9 clusters 
# s_price, apartment_size variables showed that the number of groups exceeded requirements as majority of the data overlapping
# did not perform well in property_type_id, listing_status, s_price, apartment_size

clprofiles(kpres[[7]], clust_data)
# bifurcation in apartment_size improved over the results with 9 clusters


clprofiles(kpres[[5]], clust_data)
summary(kpres[[5]])
# with 5 clusters we can clearly see the segmentation of users into various groups with least overlapping





# Export the data for further segmentation
write.csv(data, "F://JOBS//PropertyFinder//data.csv")
