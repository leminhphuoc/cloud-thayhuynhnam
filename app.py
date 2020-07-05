# =============================================================================
# from scipy import stats 
# import pandas as pd
# import datetime
# import json
# =============================================================================
import pyrebase
import HandleMissingData as handle
import numpy as np 
# =============================================================================
# import matplotlib.pyplot as plt
# import tensorflow as tf
# =============================================================================
import TempForeCast as tempfc
import HumidityForeCast as humifc
from flask import Flask,jsonify
app = Flask(__name__)
app.config["DEBUG"]= True
import json
import GetCurrent as currentLib
import os

config = {
  "apiKey": "AIzaSyDW47eqWwQOOhBhn2Ios2VeC4PoeyChBrU",
  "authDomain": "sensor-5f547.firebaseapp.com",
  "databaseURL": "https://sensor-5f547.firebaseio.com",
  "projectId": "sensor-5f547",
  "storageBucket": "sensor-5f547.appspot.com",
  "messagingSenderId": "275898920844",
  "appId": "1:275898920844:web:f93a3b640a358c565c70a9",
  "measurementId": "G-369T0R3MJ8"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

firebaseData = db.child("dht11").get().val()

df = handle.HandleMissingData(firebaseData)

temperature = np.array(df['Temperature'])
humidity = np.array(df['Humidity'])

currentTemp = currentLib.CurrentTemp(temperature)
currentHumidity = currentLib.CurrentHumidity(humidity)

tempAfter60 = tempfc.tempForeCast(temperature,float(currentTemp),60)[0][0]
humidity60 = humifc.humiForeCast(humidity,float(currentHumidity),60)[0][0]





print(currentTemp)
print(currentHumidity)

@app.route('/', methods=['GET'])
def home():
    return jsonify({"temp" : currentTemp,
    "humidity" : currentHumidity})

@app.route('/iot', methods=['GET'])
def getNextFromCurrent():
    return jsonify({"temp" : tempAfter60,
    "humidity" : humidity60})


@app.route('/iot/<float:minute>', methods=['GET'])
def iot(minute):
    tempAfterMinute = tempfc.tempForeCast(temperature,float(currentTemp),minute)[0][0]
    humidityAfterMinute = humifc.humiForeCast(humidity,float(currentHumidity),minute)[0][0]
    return jsonify({"temp" : tempAfterMinute,
    "humidity" : humidityAfterMinute})

if __name__=='__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port);












