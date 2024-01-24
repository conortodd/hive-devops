from flask import Flask, jsonify
import json
import requests
import datetime as dt


def getAverageTemp():
    #define sensors and put them in a list to iterate through
    importBox1Url="https://api.opensensemap.org/boxes/603bbc5eaf6fbf001b07a8e9"
    importBox2Url="https://api.opensensemap.org/boxes/603d471a8ad04a001b0bdccb"
    importBox3Url="https://api.opensensemap.org/boxes/603d3b2b8ad04a001b05d49c"

    urlArray=[importBox1Url,importBox2Url,importBox3Url]

    #initialize counters
    sumTemp=0
    numMesur=0

    #create function to load data as a dict
    def fetch_data(data):
        r = requests.get(data)
        return json.loads(r.content)

    #iterate through each measurement type of each sensor and find the temp and find the average of the measurements
    for url in urlArray:
        currentTime=dt.datetime.now(dt.timezone.utc)
        sensorData=fetch_data(url)
        sensorlist=sensorData['sensors']
        for item in sensorlist:
            if item['title'] == 'Temperature' or item['title']=='Temperatur':
                #do use data older than an hour
                itemTimestampStr=item['lastMeasurement']['createdAt']
                itemTimestampDt=dt.datetime.strptime(itemTimestampStr, "%Y-%m-%dT%H:%M:%S.%f%z")
                timeBound=currentTime-dt.timedelta(hours=1)
                if itemTimestampDt > timeBound:
                    temp=float(item['lastMeasurement']['value'])
                    sumTemp=sumTemp+temp
                    numMesur+=1
    averageTempVal=sumTemp/numMesur
    averageTempJSON={'AverageTemp': averageTempVal}
    return averageTempJSON