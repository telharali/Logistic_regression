# -*- coding: utf-8 -*-
"""placement.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1l_umeyX2LTznqNtgenewnAmAnJ0C4CsH
"""

import numpy as np
import pandas as pd

df= pd.read_csv("/content/placement.csv")

df

df.shape

df.head()

# prepocessing
df=df.iloc[:,1:]

df

# EDA
import matplotlib.pyplot as plt

plt.scatter(df['cgpa'],df['iq'],c=df['placement'])

# Extract input and output columns
x=df.iloc[:,0:2]
y=df.iloc[:,-1]

from sklearn.model_selection import train_test_split
x_train,x_trest,y_train,y_test=train_test_split(x,y ,test_size=0.2 ,random_state=2)

x_train

y_train

#
from sklearn.preprocessing import StandardScaler

scalar=StandardScaler()

x_train=scalar.fit_transform(x_train)

x_train

x_trest=scalar.fit_transform(x_trest)

from sklearn.linear_model import LogisticRegression

clf=LogisticRegression()

clf.fit(x_train,y_train)

y_pred=clf.predict(x_trest)

y_test

from sklearn.metrics import accuracy_score

accuracy_score(y_test,y_pred)

from mlxtend.plotting import plot_decision_regions

plot_decision_regions(x_train,y_train.values,clf=clf,legend=2)

import pickle

pickle.dump(clf,open("model.pkl","wb"))