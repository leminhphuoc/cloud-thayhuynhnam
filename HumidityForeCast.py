# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 13:33:49 2020

@author: ACER
"""
from scipy import stats 
import pandas as pd
import numpy as np 
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


def humiForeCast(humidity,currentHumidity ,minute):
    oneMinuteRecord = 15
    recordAmount = oneMinuteRecord * minute

    x_humidity = humidity[:(len(humidity)-int(recordAmount))]
    y_humidity = humidity[int(recordAmount):(len(humidity))]


    df2 = pd.DataFrame({"x" : x_humidity, "y" : y_humidity})

    size_train = int(len(df2)*0.8)

    df_train = df2[:size_train]
    df_test  = df2[size_train:]
    
    xshape = df_train['x'].array.astype(np.float).reshape(-1,1)
    yshape = df_train['y'].array.astype(np.float).reshape(-1,1)
    
    regression = LinearRegression()
    regression.fit(xshape, yshape)

    #y=Ax+B
    def f(x):
        return regression.coef_*x+regression.intercept_

    actualArray = f(df_test['x'].array.astype(np.float))
    
# =============================================================================
#     print(type(actualArray))
#     print(df_test['y'].array.astype(np.float)[:10])
#     print(actualArray[:10])
# =============================================================================
    
# =============================================================================
# =============================================================================
#     plt.scatter(df_test['x'].array.astype(np.float).reshape(-1,1), df_test['y'].array.astype(np.float).reshape(-1,1))
#     plt.plot(df_test['x'].array.astype(np.float).reshape(-1,1),actualArray.reshape(-1,1))
# =============================================================================
# =============================================================================
    
    return f(currentHumidity)

    