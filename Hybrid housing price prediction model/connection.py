#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 22:30:03 2018

@author: hassan
"""
import sqlite3 
from sqlalchemy import create_engine
engine = create_engine('sqlite:///:memory')
con = sqlite3.connect('house.db')
cur = con.cursor();
class Connection: 
    engine = create_engine('sqlite:///:memory')
    con = sqlite3.connect('house.db')
    cur = con.cursor();
    def close(self):
        cur.close();
        con.close();
        
    def get_data(self):
        import pandas as pd
        data = pd.read_sql("select * from house;",con)
        return data
          
obj =  Connection()
if obj.close == False:
   obj.close()
   print("Database is  succesafuy closed ")
else:
    print("Database is  closed")
 
    #data.to_sql("house", con, if_exists="replace")
    
   


    