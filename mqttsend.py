#!/usr/bin/python3
import paho.mqtt.client as mqtt 
import time
from datetime import timezone
from datetime import date
from datetime import datetime

mqttBroker ="mqtt" 

client = mqtt.Client("Temperature_Inside")
client.connect(mqttBroker) 

while True:
    today = datetime.now()
    dy = today.strftime("%d")
    mn =  today.strftime("%m")
    yr = today.strftime("%Y")
    hr = today.strftime("%H")
    min = today.strftime("%M")
    sec = today.strftime("%S")
    #timestamp=yr + "-" + mn + "-" + dy + " " + hr + ":" + min + ":" + sec
    timestamp=today.strftime("%Y-%m-%dT%H:%M:%S.000Z")
    #dt = datetime(int(yr), int(mn), int(dy), int(hr), int(min), int(sec))
    #timestamp = dt.replace(tzinfo=timezone.utc).timestamp()
    #timestamp=int(timestamp)
    client.publish("yotta/db/temp", str(timestamp) + "#7")
    print("Just published " + str(7) + " to topic yotta/db/temp")
    client.publish("yotta/db/humid", str(timestamp) + "#23")
    print("Just published " + str(23) + " to topic yotta/db/humid")
    time.sleep(1)
