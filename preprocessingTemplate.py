###               ###
### PREPROCESSING ###
###				  ###

#sacred source
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

	#import dataset
dataset = pd.read_csv('csv_file_name.csv')  #read_excel 
#dataset = pd.read_csv('/home/users/data.csv')
 

	#splitting dataset
X = dataset.iloc[:,:-1].values  #independent variable
Y = dataset.iloc[:,:-1].values  #dependent variable

	#dataframe slice optional
result = pd.DataFrame(data = X, index = range(len(X)), columns = ['columns1', 'columns2'])
result2 = pd.DataFrame(data = Y, index = range(len(Y)), columns = ['columns1', 'columns2'])
dataFrame = pd.concat([result, result2], axis = 1)


	#missing values  
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values = np.nan, strategy = 'mean')    
imputer = imputer.fit(x[:,:-1])
X[:,1:] = imputer.transform(X[:,1:])


	#encoder
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
X[:,0] = le.fit_transform(x[:,0])

from sklearn.preprocessing import OneHotEncoder
ohe = OneHotEncoder(categorical_features=[0])
X=ohe.fit_transform(X).toarray()

	#splitting the data set into train and test
from sklearn.cross_validation import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y,test_size=0.33, random_state=0)

	#scaling
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.fit_transform(X_test)

