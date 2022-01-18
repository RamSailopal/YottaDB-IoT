#!/usr/bin/python3
import paho.mqtt.client as mqtt
import time
import mg_python
mg_python.m_set_host(0, "yottamgweb", 7042, "", "")
def on_message(client, userdata, message):
    print("received message: " ,str(message.payload.decode("utf-8")))
    print("Writing temperature message to YottaDB")
    mess=str(message.payload.decode("utf-8")).split("#")
    mg_python.m_set(0, "^SENSORS", "temp", str(mess[0]), float(mess[1]))

mqttBroker ="test.mosquitto.org"

client = mqtt.Client()
client.connect(mqttBroker) 

client.loop_start()
while True:
   client.subscribe("yotta/db/temp")
   client.on_message=on_message 
   time.sleep(60)
