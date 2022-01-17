#!/bin/bash
python3 -m pip install paho-mqtt
python3 -m pip install Adafruit_DHT
cd /usr/local/YottaDB-IoT
./mqttsend.py &
sleep 1
./mqttrec.py &
./mqttrec1.py &
tail -f /dev/null
