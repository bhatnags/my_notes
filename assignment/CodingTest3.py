# A third question focusing on testing your modelling skills


import numpy as np
from sklearn.linear_model import LinearRegression
#from sklearn.pipeline import Pipeline
#from sklearn.preprocessing import StandardScaler
#from sklearn.svm import LinearSVC # LINEAR CLASSIFICATION


class MarketingCosts:
    # param marketing_expenditure list. Expenditure for each previous campaign.
    # param units_sold list. The number of units sold for each previous campaign.
    # param desired_units_sold int. Target number of units to sell in the new campaign.
    # returns float. Required amount of money to be invested.
    @staticmethod
    def desired_marketing_expenditure(marketing_expenditure, units_sold, desired_units_sold):
        '''myarray = np.asarray(marketing_expenditure)
        myarray.ndim
        myarray.shape
        myarray2 = np.asarray(units_sold)
        myarray2.ndim
        myarray2.shape
        X = np.vstack((myarray, myarray2)).T

        lin_reg = LinearRegression()
        lin_reg.fit(X, myarray2)
        lin_reg.predict(desired_units_sold)
        '''
        x = np.reshape(np.array(units_sold),(-1,1))
        y = np.array(marketing_expenditure)
        lin_reg = LinearRegression()
        lin_reg.fit(x, y)
        #plt.scatter(x,y)
        #plt.plot(x,body_reg.predict(x))
        a = lin_reg.predict(desired_units_sold)
        return a

#For example, with the parameters below the function should return 250000.0.
print(MarketingCosts.desired_marketing_expenditure(
    [300000, 200000, 400000, 300000, 100000],
    [60000, 50000, 90000, 80000, 30000],
    60000))	
	


# LINEAR REGRESSION
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(housing_prepared, housing_labels)

some_data = housing.iloc[:5]
some_labels = housing_labels.iloc[:5]
some_data_prepared = full_pipeline.transform(some_data)
print("Predictions:\t", lin_reg.predict(some_data_prepared))
print("Labels:\t\t", list(some_labels))

from sklearn.metrics import mean_squared_error
housing_predictions = lin_reg.predict(housing_prepared)
lin_mse = mean_squared_error(housing_labels, housing_predictions)
lin_rmse = np.sqrt(lin.mse)
lin_rmse


# DECISION TREE
from sklearn.tree import DecisionTreeRegressor
tree_reg = DecisionTreeRegressor()
tree_reg.fit(housing_prepared, housing_labels)
Now that the model is trained, let’s evaluate it on the training set:
housing_predictions = tree_reg.predict(housing_prepared)
tree_mse = mean_squared_error(housing_labels, housing_predictions)
tree_rmse = np.sqrt(tree_mse)
tree_rmse

'''
cross-validation
'''
from sklearn.model_selection import cross_val_score
''' cv=10 => randomly split the training set into 10 distinct subsets called folds, 
then it trains and evaluates the Decision Tree model 10 times,
picking a different fold for evaluation every time and training on the other 9 folds.
The result is an array containing the 10 evaluation scores:
'''
scores = cross_val_score(tree_reg, housing_prepared, housing_labels, scoring="neg_mean_squared_error", cv=10)
rmse_scores = np.sqrt(-scores)

def display_scores(scores):
	print("Scores:", scores)
	print("Mean:", scores.mean())
	print("Standard deviation:", scores.std())

display_scores(tree_rmse_scores)


# RANDOM FORREST
from sklearn.ensemble import RandomForestRegressor
forest_reg = RandomForestRegressor()
forest_reg.fit(housing_prepared, housing_labels)
forest_rmse
display_scores(forest_rmse_scores)




'''
SVN
'''
import numpy as np
from sklearn import datasets
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC # LINEAR CLASSIFICATION
iris = datasets.load_iris()
X = iris["data"][:, (2, 3)] # petal length, petal width
y = (iris["target"] == 2).astype(np.float64) # Iris-Virginica
svm_clf = Pipeline(
		("scaler", StandardScaler()),
		("linear_svc", LinearSVC(C=1, loss="hinge")),
		)
svm_clf.fit(X_scaled, y)

svm_clf.predict([[5.5, 1.7]])


from sklearn.datasets import make_moons
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures # NON LINEAR CLASSIFICATION
polynomial_svm_clf = Pipeline((
		("poly_features", PolynomialFeatures(degree=3)),
		("scaler", StandardScaler()),
		("svm_clf", LinearSVC(C=10, loss="hinge"))
		))
polynomial_svm_clf.fit(X, y)


# Polinomial Kernel
from sklearn.svm import SVC
poly_kernel_svm_clf = Pipeline((
	("scaler", StandardScaler()),
	("svm_clf", SVC(kernel="poly", degree=3, coef0=1, C=5))
))
poly_kernel_svm_clf.fit(X, y)


# LINEAR REGRESSION
from sklearn.svm import LinearSVR
svm_reg = LinearSVR(epsilon=1.5)
svm_reg.fit(X, y)


# NON LINEAR REGRESSION
from sklearn.svm import SVR
svm_poly_reg = SVR(kernel="poly", degree=2, C=100, epsilon=0.1)
svm_poly_reg.fit(X, y)

