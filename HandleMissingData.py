# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 10:11:28 2020

@author: ACER
"""

import pandas as pd

def HandleMissingData(firebaseData):
    temp = list()
    humidity = list()
    datetime = list()
    for item in firebaseData:
        temp.append(item['temperature'])
        humidity.append(item['humidity'])
        datetime.append(item['datetime'])

    df = pd.DataFrame({"Temperature" : temp, "Humidity" : humidity, "Datetime" : datetime})
    df.to_csv ('FireBaseData.csv', index = None)

    df2 = pd.read_csv('FireBaseData.csv',header = 0, delimiter = ',')
    
    
    df2['Temperature'].fillna(method = 'ffill', inplace = True)
    df2['Temperature'].fillna(method = 'bfill', inplace = True)
    df2['Humidity'].fillna(method = 'ffill', inplace = True)
    df2['Humidity'].fillna(method = 'bfill', inplace = True)
    df2['Datetime'].fillna(method = 'ffill', inplace = True)
    df2['Datetime'].fillna(method = 'bfill', inplace = True)

    return df
