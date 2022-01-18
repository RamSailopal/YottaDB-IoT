#!/usr/bin/python3
import paho.mqtt.client as mqtt 
import time
import os
import sys
from datetime import timezone
from datetime import date
from datetime import datetime


mqttBroker = "test.mosquitto.org"

client = mqtt.Client("Sensor")
client.connect(mqttBroker) 

while True:
    today = datetime.now()
    dy = today.strftime("%d")
    mn =  today.strftime("%m")
    yr = today.strftime("%Y")
    hr = today.strftime("%H")
    min = today.strftime("%M")
    sec = today.strftime("%S")
    timestamp=today.strftime("%Y-%m-%dT%H:%M:%S.000Z")
    client.publish("yotta/db/temp", str(timestamp) + "#7")
    print("Just published " + str(7) + " to topic yotta/db/temp")
    client.publish("yotta/db/humid", str(timestamp) + "#23")
    print("Just published " + str(23) + " to topic yotta/db/humid")
 
    time.sleep(60)
