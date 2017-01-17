"""
Module Name:  d2cMsgSender.py
Project:      IoTHubRestSample
Copyright (c) Microsoft Corporation.
Using [Send device-to-cloud message](https://msdn.microsoft.com/en-US/library/azure/mt590784.aspx) API to send device-to-cloud message from the simulated device application to IoT Hub.
This source is subject to the Microsoft Public License.
See http://www.microsoft.com/en-us/openness/licenses.aspx#MPL
All other rights reserved.
THIS CODE AND INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, 
EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED 
WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A PARTICULAR PURPOSE.
"""
from json import JSONEncoder
import base64
import hmac
import hashlib
import time
import datetime
import requests
import urllib
import os
import glob
import time


class D2CMsgSender:
    
    API_VERSION = '2016-02-03'
    TOKEN_VALID_SECS = 10
    TOKEN_FORMAT = 'SharedAccessSignature sig=%s&se=%s&skn=%s&sr=%s'

    def __init__(self, connectionString=None):
        if connectionString != None:
            iotHost, keyName, keyValue = [sub[sub.index('=') + 1:] for sub in connectionString.split(";")]
            self.iotHost = iotHost
            self.keyName = keyName
            self.keyValue = keyValue
            
    def _buildExpiryOn(self):
        return '%d' % (time.time() + self.TOKEN_VALID_SECS)
    
    def _buildIoTHubSasToken(self, deviceId):
        resourceUri = '%s/devices/%s' % (self.iotHost, deviceId)
        targetUri = resourceUri.lower()
        expiryTime = self._buildExpiryOn()
        toSign = '%s\n%s' % (targetUri, expiryTime)
        key = base64.b64decode(self.keyValue.encode('utf-8'))
        signature = urllib.quote(
            base64.b64encode(
                hmac.HMAC(key, toSign.encode('utf-8'), hashlib.sha256).digest()
            )
        ).replace('/', '%2F')
        return self.TOKEN_FORMAT % (signature, expiryTime, self.keyName, targetUri)
    
    def sendD2CMsg(self, deviceId, message):
        sasToken = self._buildIoTHubSasToken(deviceId)
        url = 'https://%s/devices/%s/messages/events?api-version=%s' % (self.iotHost, deviceId, self.API_VERSION)
        r = requests.post(url, headers={'Authorization': sasToken}, data=message)
        return r.text, r.status_code

class TempHumReader:

    def read_data(self):
        #Reads the sensor data of the DHT22
        #and returns a temperature and a humidity value

        #TBD
        temperature_fahrenheit = 60 #Real Sensor Data
        humidity = 50 #Real Sensor Data
        
        return temperature_fahrenheit, humidity
    
if __name__ == '__main__':
    connectionString = 'HostName=TempHumHub.azure-devices.net;SharedAccessKeyName=iothubowner;SharedAccessKey=qiAPlJiP0KfKHXoTP1/3A8x3YF7PC6jPBa9HrH6HIiQ='
    d2cMsgSender = D2CMsgSender(connectionString)
    deviceId = 'IOT-GNS-Temperature-2'

    try:
        while True:
            tempHumSensor = TempHumReader()
            temperature_fahrenheit, humidity = tempHumSensor.read_data()

            time_seconds = time.time()
            timestamp = datetime.datetime.fromtimestamp(time_seconds).strftime('%Y-%m-%d %H:%M:%S')
     
            jsonString = JSONEncoder().encode({
                "rcd_type": "Temp",  #Don't know what this means
                "source_device":deviceId,
                "temperature": temperature_fahrenheit,
                "humidity": humidity,
                "timestamp":timestamp
            })
            print jsonString
            message = jsonString
            print d2cMsgSender.sendD2CMsg(deviceId, message)
            time.sleep(5)
    except:
        print "Ende"
