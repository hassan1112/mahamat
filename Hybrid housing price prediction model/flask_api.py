#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 20:04:04 2018

@author: hassan
"""


from flask import Flask,jsonify,request,render_template
import numpy as np
import pickle 
import json
import flask
import pandas as pd


app = Flask(__name__)

@app.route("/index")
def index():
    return flask.render_template('index.php')
    

#price,bedrooms,bathrooms,sqft_living,sqft_lot,floors,condition,sqft_above,sqft_basement,yr_built,zipcode,lat,long,cluster

@app.route("/process",methods=['POST'])
def process():
    bedrooms = request.form.get('bedrooms') 
    bathrooms = request.form.get('bathrooms')
    sqft_living = request.form.get('sqft_living')
    
    sqft_lot = request.form.get('sqft_lot') 
    floors = request.form.get('floors')  
    condition = request.form.get('condition')         
    
    sqft_above = request.form.get('sqft_above') 
    sqft_basement =  request.form.get('sqft_basement')
    yr_built =  request.form.get('yr_built')
    
    zipcode = request.form.get('zipcode')    
    long = request.form.get('long') 
    lat =  request.form.get('lat')
        
    dict = {"bedrooms":bedrooms,"bathrooms":bathrooms,"sqft_living":sqft_living,"sqf_lot":sqft_lot,"floors":floors,"condition":condition,"sqft_above":sqft_above,"sqft_basement":sqft_basement,"yr_built":yr_built,"zipcode":zipcode,"lat":lat,"long":long,"cluster":0}
    df = pd.DataFrame(dict,index=[0],columns=dict.keys())
    df.to_csv("requested.csv")
    try:    
        if (int(df["yr_built"]) != 0 and int(df["sqft_living"]) != 0 and int(df["condition"]) != 0 and float(df["lat"]) != 0 and float(df["long"]) != 0 and int(df["zipcode"]) != 0): 
            data = pd.read_csv("requested.csv")
            model = pickle.load(open("trained_model.pkl","br"))
            price = model.predict(df)
            r = pd.DataFrame(price)
            r.reset_index(drop=True,inplace=True)
            r.to_csv("result.csv")
            
            r = int(r.iloc[0,0])
            price = int(price)
            v = "{0} USD".format(r)
            
            t = "Predicted price is :"
            
            return flask.render_template('index.php',variable = v,txt=t)
        else:
            return flask.render_template('index.php',variable="Request can not be served, Please provide valid data")
    except:
        return flask.render_template('index.php',variable="Request can not be served,please supply numerical data")

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8001, debug=True)

