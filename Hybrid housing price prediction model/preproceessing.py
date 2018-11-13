#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: hassan

"""
from modules import *
data = pd.read_csv("houses_data.csv")
x_var = data.iloc[:,1:]
y_var = data.iloc[:,0]
columns = data.columns.values

from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
imputer = imputer.fit(x_var[:, 2:])
x_var[:, 2:] = imputer.transform(x_var[:, 2:])

# Encoding categorical data
# Encoding the Independent Variable
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_x_var = LabelEncoder()
x_var[:, 9] = labelencoder_x_var.fit_transform(x_var[:, 9])

# Encoding the Dependent Variable
labelencoder_y = LabelEncoder()
y_var = labelencoder_y.fit_transform(y)


class preprocess:
    try:
        columns = data.columns.values
        for column in columns:
            def convert(self,col):
                if col in columns:
                    data[col] = data[col].astype(np.int32)
                    print("{0} converted to int32 successfully".format(col));
                else:
                    print("please! provide correct  column name  : ")



        columns = data.columns.values
        for column in columns:
            def discard(self,col,axs):
                if col in columns:
                    Inplace=True
                    data.drop([col],axis=axs,inplace=Inplace)
                    print("{0} deleted successfully".format(col));
                else:
                    print("please! provide correct  column name  :  ")
       
         new_data = pd.DataFrame()
        def select_rows(n,data):
            if data.empty:
                print("the data object does contain any observation")
            else:
                 new_data = data.head(n)
                 print(new_data)


conv = preprocess()
col = input("Enter the name of the column to be converted into int32")
conv.convert(col)

delete  = preprocess()
col = input("Enter the name of the column")
conf = input("are you sure want to delete [y|n] ? \n")
if(conf == 'y'):
    delete.discard(col,1)
else:
    pass
    
select_rows(1000,data)
print(new_data)

