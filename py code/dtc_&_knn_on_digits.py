# -*- coding: utf-8 -*-
"""DTC_&_KNN_on_Digits.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GQF3WyUEy_07ABfePV1GFAm3NwQ1GSZ0
"""

# importing Digits data
from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Loading Digit Dataset
digit_data=load_digits()

# Fetching information of Digit Dataset
dir(digit_data)

# Training data
features=digit_data.data
features.shape  # Getting Rows and Columns

# Answer to Data
label=digit_data.target   # Answers of the training data
label.shape  # Getting Rows and Columns
label

# Images data stored in dataset
images=digit_data.images  
images[0]  # Data of the image '0'. ex- images[5] - data of the image '5'

# Visualizing the image data...
plt.imshow(images[4])   # this is how the number '4' image data looks like.

# Splitting the data..
train_data,test_data,train_label,test_label = train_test_split(features,label,test_size=0.1)

"""***Applying Decision Tree Classifier***"""

# Calling the Decision Tree Classifier
from sklearn.tree import DecisionTreeClassifier
clf=DecisionTreeClassifier()

# Training the data
trained=clf.fit(train_data,train_label)

# Predicting the Data
dtcpredicted=trained.predict(test_data)

# Calculating the accuracy score
dtc=accuracy_score(dtcpredicted,test_label)
dtc

"""Applying KNN Classifier"""

# Now applying KNN Classifier on the same dataset
from sklearn.neighbors import KNeighborsClassifier
kclf=KNeighborsClassifier(n_neighbors=5)

# Now Training the data
ktrained=kclf.fit(train_data,train_label)

# Now predicting
kpredicted=ktrained.predict(test_data)

# Calculating the Accuracy Score
knnc=accuracy_score(kpredicted,test_label)
knnc

# Visualizing the accuracy score of both Classifiers
plt.ylabel("Accuracy Level")
plt.xlim(0,4)
plt.bar([1],[knnc], label="KNN Accuracy")
plt.bar([2],[dtc],label="DecisionTree Accuracy")
plt.grid()
plt.legend()

