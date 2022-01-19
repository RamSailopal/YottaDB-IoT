#!/bin/bash
apt-get update
apt-get install -y rpi.gpio python3
python3 -m pip install paho-mqtt
python3 -m pip install Adafruit_DHT


