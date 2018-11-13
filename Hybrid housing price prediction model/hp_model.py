#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 16:31:26 2018
@author: hassan
"""


from modules import *
from connection import *
import tkinter
from tkinter import *
from matplotlib.pyplot import *
from sklearn.metrics import r2_score
from sklearn.externals import joblib
import pickle


con = Connection()
try:
    data= con.get_data()
    

except Exception as err:
    print("{0}".format(err))
   
    
finally:
    con.con.close()
   # con.cur.close()
    print("Database is  succesafuy closed ")
    
data = data.iloc[:,1:]    
print("\nEnd of Reading the data from sqlite3 house table ")
data.head()

data= data.sort_values(["price"],ascending=TRUE)
data.reset_index(drop=True,inplace=True)

data.to_csv("sorted_data.csv")
y = data['price']

x = data.iloc[:,1:]

model = LinearRegression()
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=0)
model.fit(x_train,y_train)
y_pred = model.predict(x_test)


#serializing our model to a file called model.pkl
pickle.dump(model, open("LR_model.pkl","wb"))

#loading a model from a file called model.pkl
model = pickle.load(open("LR_model.pkl","rb"))
