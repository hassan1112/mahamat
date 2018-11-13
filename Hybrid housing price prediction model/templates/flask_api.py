#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 20:04:04 2018

@author: hassan
"""

from flask import Flask,jsonify,request,render_template
import numpy as np
import pickle 
import flask
import pandas as pd
model = pickle.load(open("LR_model.pkl","br"))
app = Flask(__name__)
@app.route("/")
@app.route("/index",methods=["POST"])
def index():
    return flask.render_template('index.php')
    data1 = request.get_json(force=True)
    data = pd.read_json(data1,orient='records')
    data.to_csv("new.csv")
# =============================================================================
# # =============================================================================

    # predict_request = [data["bedrooms"], data["bathrooms"],data["sqft_living"], data["sqft_lot"],data["floors"],
     #   ["condition"], ["sqft_above"], ["sqft_basement"], ["yr_built"], ["zipcode"],
     # ["lat"], ["long"], ["cluster"]]
#

     #https://www.youtube.com/watch?v=RbejfDTHhhg
# # =============================================================================
    predict_request = np.array(data)
# =============================================================================
    price = model.predict(predict_request)
    output = [price[0]]
    return jsonify(resul=output)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)


