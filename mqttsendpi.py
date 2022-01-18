#!/usr/bin/python3
import paho.mqtt.client as mqtt 
import Adafruit_DHT
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
    sensor=Adafruit_DHT.DHT11
    gpio=17
    humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)
    if humidity is not None and temperature is not None:
       print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
       client.publish("yotta/db/temp", str(timestamp) + "{0:0.1f}".format(temperature))
       client.publish("yotta/db/temp", str(timestamp) + "{0:0.1f}".format(humidity))
    else:
       print('Failed to get reading. Try again!')
 
    time.sleep(60)
