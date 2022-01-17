#!/bin/bash
yum update -y
yum install -y git gcc
cd /usr/local
git clone https://github.com/adafruit/Adafruit_Python_DHT.git
cd /usr/local/Adafruit_Python_DHT
python3 setup.py install --force-pi
python3 -m pip install paho-mqtt
cd /usr/local/YottaDB-IoT
./mqttsend.py &
sleep 1
./mqttrec.py &
./mqttrec1.py & 
tail -f /dev/null
