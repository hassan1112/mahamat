#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 18:50:14 2018

@author: hassan
"""

from modules import *
from connection import *
import tkinter
from tkinter import *
from matplotlib.pyplot import *
from sklearn.metrics import r2_score
import pickle
from sklearn.metrics import mean_squared_error

con = Connection()
try:
    data= con.get_data()
    
except Exception as err:
    print("{0}".format(err))

finally:
    con.close()
    print("Database is  succesafuy closed ")
    
    
data = data.iloc[:,1:]    
print("\nEnd of Reading the data from sqlite3 house table ")
data.head()

data= data.sort_values(["price"],ascending=TRUE)
data.reset_index(drop=True,inplace=True)

data.to_csv("sorted_data.csv")

y = data['price']
x = data.iloc[:,1:]
clustered_data = x

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=0)

class model_evaluation:
            
    def rmse(y_test, y_pred):
        '''Root Mean Square error :'''
        rmse = np.sqrt(sum((y_test - y_pred) ** 2) / len(y_test))
        return rmse
    
    
    def r2_score(y_test, y_pred):
        '''Model Evaluation - R2 Score :'''
        mean_y = np.mean(y)
        ss_tot = sum((y_test - mean_y) ** 2)
        ss_res = sum((y_test - y_pred) ** 2)
        r2 = 1 - (ss_res / ss_tot)
        return r2
     
    def sse(y_test, y_pred):
        '''Model Evaluation - sse Score :'''
        result = np.sum((y_test - y_pred) ** 2)
        
        return result
evaluation = model_evaluation()
print("\n\n")
gradientdescent = ensemble.GradientBoostingRegressor()
gradientdescent.fit(x_train, y_train)
y_pred2 = gradientdescent.predict(x_test)
print("\n"*2)
print("----MLR with gradient descent----")
print("Residual errors")
print("\t\t MSE {0}".format(mean_squared_error(y_test, y_pred2)))
print("\t\t RMSE {0}".format(model_evaluation.rmse(y_test, y_pred2)))
print("\t\t SSE {0}".format(model_evaluation.sse(y_test, y_pred2)))
print("\n\n Explained variance\n")
print("\t\t r2 {0}".format(model_evaluation.r2_score(y_test, y_pred2)))
pickle.dump(gradientdescent, open("trained_model.pkl","wb"))
