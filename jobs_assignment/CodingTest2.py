# A second question focusing on your data processing skills
# Chapter 2

# Get the data
import os
import tarfile
from six.moves import urllib

DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml/master/"
HOUSING_PATH = "datasets/housing"
HOUSING_URL = DOWNLOAD_ROOT + HOUSING_PATH + "/housing.tgz"

def fetch_housing_data(housing_url=HOUSING_URL, housing_path=HOUSING_PATH):
	if not os.path.isdir(housing_path):
		os.makedirs(housing_path)
	tgz_path = os.path.join(housing_path, "housing.tgz")
	urllib.request.urlretrieve(housing_url, tgz_path)
	housing_tgz = tarfile.open(tgz_path)
	housing_tgz.extractall(path=housing_path)
	housing_tgz.close()

import pandas as pd
def load_housing_data(housing_path=HOUSING_PATH):
	csv_path = os.path.join(housing_path, "housing.csv")
	return pd.read_csv(csv_path)

# Describe the data
housing = load_housing_data()
housing.head()
housing.info()
housing.describe()
# Get categories
housing["ocean_proximity"].value_counts()

# Data Visualization - I
%matplotlib inline # only in a Jupyter notebook
import matplotlib.pyplot as plt
housing.hist(bins=50, figsize=(20,15))
plt.show()

# Split Test/Train datasets
import numpy as np
def split_train_test(data, test_ratio):
	shuffled_indices = np.random.permutation(len(data))
	test_set_size = int(len(data) * test_ratio)
	test_indices = shuffled_indices[:test_set_size]
	train_indices = shuffled_indices[test_set_size:]
	return data.iloc[train_indices], data.iloc[test_indices]
train_set, test_set = split_train_test(housing, 0.2)
print(len(train_set), "train +", len(test_set), "test")

# OR
import hashlib
def test_set_check(identifier, test_ratio, hash):
	return hash(np.int64(identifier)).digest()[-1] < 256 * test_ratio
def split_train_test_by_id(data, test_ratio, id_column, hash=hashlib.md5):
	ids = data[id_column]
	in_test_set = ids.apply(lambda id_: test_set_check(id_, test_ratio, hash))
	return data.loc[~in_test_set], data.loc[in_test_set]
housing_with_id = housing.reset_index() # adds an `index` column
train_set, test_set = split_train_test_by_id(housing_with_id, 0.2, "index")
# OR
housing_with_id["id"] = housing["longitude"] * 1000 + housing["latitude"]
train_set, test_set = split_train_test_by_id(housing_with_id, 0.2, "id")

# OR
from sklearn.model_selection import train_test_split
train_set, test_set = train_test_split(housing, test_size=0.2, random_state=42)


# OR
from sklearn.model_selection import StratifiedShuffleSplit
split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
for train_index, test_index in split.split(housing, housing["income_cat"]):
	strat_train_set = housing.loc[train_index]
	strat_test_set = housing.loc[test_index]

# Create a copy of the dataset created
housing = strat_train_set.copy()

# Data Visualization - II
housing.plot(kind="scatter", x="longitude", y="latitude")
#Setting the alpha option to 0.1 makes it much easier to visualize the places where there is a high density of data points
housing.plot(kind="scatter", x="longitude", y="latitude", alpha=0.1)
# OR
housing.plot(kind="scatter", x="longitude", y="latitude", alpha=0.4, s=housing["population"]/100, 
label="population",c="median_house_value", cmap=plt.get_cmap("jet"), colorbar=True, )
plt.legend()

# Understanding data using Correlations (Pearson's r) - I
corr_matrix = housing.corr()
# OR
corr_matrix["median_house_value"].sort_values(ascending=False)


# Data Visualization III
from pandas.tools.plotting import scatter_matrix
attributes = ["median_house_value", "median_income", "total_rooms", "housing_median_age"]
scatter_matrix(housing[attributes], figsize=(12, 8))


# Data Visualization IV
housing.plot(kind="scatter", x="median_income", y="median_house_value", alpha=0.1)


# Experimenting with variable combinations
housing["rooms_per_household"] = housing["total_rooms"]/housing["households"]
housing["bedrooms_per_room"] = housing["total_bedrooms"]/housing["total_rooms"]
housing["population_per_household"]=housing["population"]/housing["households"]


# Understanding data using Correlations (Pearson's r) - II
corr_matrix = housing.corr()
corr_matrix["median_house_value"].sort_values(ascending=False)


# Data Cleaning
housing = strat_train_set.drop("median_house_value", axis=1)
housing_labels = strat_train_set["median_house_value"].copy()

# Cleaning column with NA values
housing.dropna(subset=["total_bedrooms"]) # option 1
housing.drop("total_bedrooms", axis=1) # option 2
median = housing["total_bedrooms"].median()
housing["total_bedrooms"].fillna(median) # option 3
#OR
from sklearn.preprocessing import Imputer
# replace each attribute’s missing values with the median of that attribute:
imputer = Imputer(strategy="median")
# median can only be computed on numerical attributes => create a copy of the data without the text attribute ocean_proximity:
housing_num = housing.drop("ocean_proximity", axis=1)
# simply computed the median of each attribute and stored the result in its statistics_
imputer.fit(housing_num)
imputer.statistics_
housing_num.median().values
# use the “trained” imputer to transform the training set by replacing missing values by the learned medians:
X = imputer.transform(housing_num)
# Above X is a plain Numpy array, put it back into a Pandas DataFrame
housing_tr = pd.DataFrame(X, columns=housing_num.columns)



# Handling Text and Categorical Attributes
from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()
housing_cat = housing["ocean_proximity"]
housing_cat_encoded = encoder.fit_transform(housing_cat)
housing_cat_encoded
print(encoder.classes_)

# OR
from sklearn.preprocessing import OneHotEncoder
encoder = OneHotEncoder()
housing_cat_1hot = encoder.fit_transform(housing_cat_encoded.reshape(-1,1))
housing_cat_1hot
housing_cat_1hot.toarray()

# OR
from sklearn.preprocessing import LabelBinarizer
encoder = LabelBinarizer()
housing_cat_1hot = encoder.fit_transform(housing_cat)
housing_cat_1hot























from sklearn.base import BaseEstimator, TransformerMixin
rooms_ix, bedrooms_ix, population_ix, household_ix = 3, 4, 5, 6
class CombinedAttributesAdder(BaseEstimator, TransformerMixin):
	def __init__(self, add_bedrooms_per_room = True): # no *args or **kargs
		self.add_bedrooms_per_room = add_bedrooms_per_room

	def fit(self, X, y=None):
		return self # nothing else to do

	def transform(self, X, y=None):
		rooms_per_household = X[:, rooms_ix] / X[:, household_ix]
		population_per_household = X[:, population_ix] / X[:, household_ix]
		if self.add_bedrooms_per_room:
			bedrooms_per_room = X[:, bedrooms_ix] / X[:, rooms_ix]
			return np.c_[X, rooms_per_household, population_per_household, bedrooms_per_room]
		else:
			return np.c_[X, rooms_per_household, population_per_household]
attr_adder = CombinedAttributesAdder(add_bedrooms_per_room=False)
housing_extra_attribs = attr_adder.transform(housing.values)






'''
PIPELINES
'''
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
num_pipeline = Pipeline([
	('imputer', Imputer(strategy="median")),
	('attribs_adder', CombinedAttributesAdder()),
	('std_scaler', StandardScaler()),
	])
housing_num_tr = num_pipeline.fit_transform(housing_num)



from sklearn.pipeline import FeatureUnion
num_attribs = list(housing_num)
cat_attribs = ["ocean_proximity"]
num_pipeline = Pipeline([
		('selector', DataFrameSelector(num_attribs)),
		('imputer', Imputer(strategy="median")),
		('attribs_adder', CombinedAttributesAdder()),
		('std_scaler', StandardScaler()),
		])
cat_pipeline = Pipeline([
		('selector', DataFrameSelector(cat_attribs)),
		('label_binarizer', LabelBinarizer()),
		])
full_pipeline = FeatureUnion(transformer_list=[
		("num_pipeline", num_pipeline),
		("cat_pipeline", cat_pipeline),
		])



housing_prepared = full_pipeline.fit_transform(housing)
housing_prepared
housing_prepared.shape





from sklearn.base import BaseEstimator, TransformerMixin
class DataFrameSelector(BaseEstimator, TransformerMixin):
	def __init__(self, attribute_names):
		self.attribute_names = attribute_names
	def fit(self, X, y=None):
		return self
	def transform(self, X):
		return X[self.attribute_names].values
dfs = DataFrameSelector(attribute_names)
iDontKNow = dfs.transform(housing.something)



# Select & train the model




