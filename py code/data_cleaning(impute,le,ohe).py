# -*- coding: utf-8 -*-
"""data_cleaning(Impute,LE,OHE).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qu6j_key5_2HE7cxuG8DqVgu3LtqRpD_
"""

import pandas as pd

# Reading CSV file from URL
df=pd.read_csv('info.csv')

df.info()

df

# To get description about columns like mean, min, max...
df.describe()

x=df.iloc[:,0:4].values

"""***IMPUTATION***"""

# Removing missing values or replacing missing value with some relevant data we use IMPUTER
from sklearn.preprocessing import Imputer

imp=Imputer(missing_values='NaN',axis=0,strategy='most_frequent')     # axis=0 - Check column wise. # strategy='mean/min/max' - replace the missing value with the mean.

impute=imp.fit(x[:,1:3])    # This is only fitting of columns that we want to process

# Now time for transforming the fitted columns
x[:,1:3]=impute.transform(x[:,1:3])    # also replacing the missing values
x

"""***LABEL ENCODING (LE)***"""

# Labelling the string type of data into INT/FLOAT , because classifier requires int/float values
from sklearn.preprocessing import LabelEncoder
cont=LabelEncoder()   # This is for labelling the country column

# Now Applying the column to the LabelEncoder ( Here Country column)
x[:,0]=cont.fit_transform(x[:,0])
x

purchase=LabelEncoder()
x[:,3]=purchase.fit_transform(x[:,3])
x

"""***ONE HOT ENCODING (OHE)***"""

# --------Feature Scaling ---------
# Now enecoding first column  -- making subcolumns of first column..
# Why we do this :-  because while applying KNN like algorithm if we convert some value into number like country in 0,1,2... 
#      so in this case while calculating distance (x^2-x^1) if x=0 then machine will assume that x has no value, this will impact the model..

from sklearn.preprocessing import OneHotEncoder

# Defining exact column number where we want to make category
firstclm = OneHotEncoder(categorical_features=[0])  # 0 - The column where to apply

x=firstclm.fit_transform(x).toarray()    # After Transformation we need to convert into numpy array
x

x.astype(int)    # To display in integer only.

