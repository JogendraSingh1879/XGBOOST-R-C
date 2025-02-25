# -*- coding: utf-8 -*-
"""XGBoost_Classifier.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1CpNc_tHuu26lUmpNHCP57vs5Dlj0PwQr
"""

#Installing XGBoost
!pip install xgboost

#importing library
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from xgboost import XGBClassifier

#Uploading the data
from google.colab import files
uploaded = files.upload()

#getting the data into a dataframe
df = pd.read_csv('pima-indians-diabetes.csv', names=['Pregnencies', 'Glucose','bloodPressure','SkinThickness','Insulin', 'BMI', 'DiebetesPedigreeFunction', 'Age','Outcome'])

df.head()

# Separating training and testing data
X = df.drop('Outcome', axis =1)
y = df['Outcome']

# Performing train test split

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=42)

#Fitting the model
model = XGBClassifier()
model.fit(X_train, y_train)

#Taking prediction from the data
y_pred = model.predict(X_test)

#Evaluating the model
from sklearn import metrics
print('Accuracy :', np.round(metrics.accuracy_score(y_test, y_pred),2))
print('Precision :', np.round(metrics.precision_score(y_test, y_pred),2))
print('Recall :', np.round(metrics.recall_score(y_test, y_pred),2))
print('F1 Score :', np.round(metrics.f1_score(y_test, y_pred),2))