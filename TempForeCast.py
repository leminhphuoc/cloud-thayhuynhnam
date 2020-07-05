# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 13:33:49 2020

@author: ACER
"""
import pandas as pd
import numpy as np 
from sklearn.linear_model import LinearRegression


def tempForeCast(temperature,currentTemp ,minute):
    oneMinuteRecord = 15
    recordAmount = oneMinuteRecord * minute

    x_temp = temperature[:(len(temperature)-int(recordAmount))]
    y_temp = temperature[int(recordAmount):(len(temperature))]


    df2 = pd.DataFrame({"x" : x_temp, "y" : y_temp})

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

# =============================================================================
#     actualArray = f(df_test['x'].array.astype(np.float))
# =============================================================================
    
# =============================================================================
#     print(type(actualArray))
#     print(df_test['y'].array.astype(np.float)[:10])
#     print(actualArray[:10])
#     
# =============================================================================
# =============================================================================
# =============================================================================
#     plt.plot(df_test['x'].array.astype(np.float).reshape(-1,1), df_test['y'].array.astype(np.float).reshape(-1,1))
#     plt.plot(df_test['x'].array.astype(np.float).reshape(-1,1),actualArray.reshape(-1,1))
# =============================================================================
# =============================================================================
    
    return f(currentTemp)

    