#!/usr/bin/python3
import paho.mqtt.client as mqtt
import time
import mg_python
mg_python.m_set_host(0, "yottamgweb", 7042, "", "")
def on_message(client, userdata, message):
    print("received message: " ,str(message.payload.decode("utf-8")))
    print("Writing humidity message to YottaDB")
    mess=str(message.payload.decode("utf-8")).split("#")
    mg_python.m_set(0, "^SENSORS", "humid", str(mess[0]), int(mess[1]))

mqttBroker ="mqtt"

client = mqtt.Client("Pi")
client.connect(mqttBroker) 

client.loop_start()

client.subscribe("yotta/db/humid")
client.on_message=on_message 

time.sleep(30)
client.loop_stop()
