#!/usr/bin/env python
# coding: utf-8


# Import packages
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Load data
data = pd.read_csv("mtcars.csv")

x_train = data.drop(['model', 'mpg','cyl','vs','am','gear','carb'],axis=1)
y_train=data['mpg']

# build linear model

model_mpg = LinearRegression().fit(x_train, y_train)

# Predictors
col_imp = [ "disp", "hp", "drat", "wt", "qsec"]

def predict(dict_values, col_imp = col_imp):
    x = np.array([float(dict_values[col]) for col in col_imp])
    x = x.reshape(1,-1)
    y_pred = model_mpg.predict(x)[0]
    return y_pred

