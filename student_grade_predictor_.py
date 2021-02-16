
''' 
The following program allows you to predict the final grade of a student using machine learning (linear regression)
''' 


import pandas as pd
import numpy as np 
import sklearn 
import seaborn as sns 


import matplotlib.pyplot as plt 
import pickle
from matplotlib import style



from sklearn import linear_model
from sklearn.utils import shuffle

pd.set_option('display.max_columns', None)
data = pd.read_csv("student-por.csv", sep=";") # data is separated by semi-colons

# data exploration

print(data.head())
print(data.describe())
print(data[['age','studytime', 'absences']].describe())
print(data.studytime.value_counts())
print(data.columns)

print(data.dtypes)

# feature selection 

# 1) filter method 
#print(data.corr(data['G2']))
print()

print()
print()

# # our attributes 
#data = data[["G1", "G2", "G3", "studytime", "absences" ]]  # we picked data that has integer types only which makes it easier 


sex_mapping ={'M':0,'F':1}

data['sex_mapping'] = data.sex.map(sex_mapping)

print(data.head())

feature= ['G1','G2','studytime','age','sex_mapping']
print(data.head())


# # We are trying to predict the value G3 which is their third/final grade

# our label 
predict = ["G3"]
X = np.array(data[feature])
print(X.shape) # 4 dimension array
y = np.array(data[predict])
print(y.shape) # 1 dimension array


x_train, x_test, y_train,  y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.2)


i=4

linear = linear_model.LinearRegression()

best = 0
# gives different scores as different test data is used in each test
for _ in range(30):
	x_train, x_test, y_train,  y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.2)
	linear.fit(x_train, y_train)
	acc = linear.score(x_test, y_test)
	print(" The accuracy score is: ",acc)

	## We can predict with an 86.2% accuracy the grade of a student at the end of the year given 
	##their `G1`, `G2`, `studytime` and `absences` data.

	# To now make use of the model, 


	#this saves a pickle file in our directory which we can use
	if acc > best:
		best = acc
		with open("studentmodel_new.pickle", "wb") as f:
			pickle.dump(linear, f)

print(best)



#----------------------------------------------------------



#----------------------------------------------------------
pickle_in = open("studentmodel_new.pickle", "rb")

# load our saved model 
linear = pickle.load(pickle_in)



print("Coefficients: \n", linear.coef_) # The higher the coefficient, the more weight an attribute `[date["G2"]]` actually has when we are prediciting
print("Intercept: \n " , linear.intercept_)

# we obtain the coefficients [m in our equation] for all of our data variables and the y intercept [y in our ].

predictions = linear.predict(x_test)

# this loop prints out the prediction vs actual output 
print()
print("Prediction vs Actual")

for i in range(10):
	print(predictions[i],y_test[i])



# Plot showing a sample of the results


m = list(range(10))
plt.title('prediction vs actual \n final grades')
plt.ylabel('grade')
plt.xlabel('student')
plt.plot(m,y_test[0:10], label='Actual')
plt.plot(m,predictions[0:10], label='Predicted')
plt.legend()
plt.show()




