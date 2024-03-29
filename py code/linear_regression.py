# -*- coding: utf-8 -*-
"""linear_regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_15Wa_-EEXG8E5SLVfT6X2A1LlT0bbKl
"""

import pandas as pd
import matplotlib.pyplot as plt

# Loading the data
df=pd.read_csv('salary.csv')

# Reading schema
df.info()

df.head(5)

# Experience that we are going to use as input of training data..
exp=df.iloc[:,0:1].values

# Salary 
sal=df.iloc[:,1:2].values

# Now we can visualize this experience and salary data
plt.xlabel('Experience')
plt.ylabel('Salary')
plt.scatter(exp,sal)

# Calling linear regression model ..  
from sklearn.linear_model import LinearRegression

# Model creation
regr=LinearRegression()

# Fitting experience and salary
trained=regr.fit(exp,sal)

# Now predicting
predicted=trained.predict(exp)

plt.xlabel('Experience')
plt.ylabel('Salary')
plt.scatter(exp,sal,label="actual data as per exp")
plt.plot(exp,trained.predict(exp),label="predicted salary")
plt.legend()
plt.show()

