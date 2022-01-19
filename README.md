# YottaDB-IoT

![Alt text](raspberrypi.jpg?raw=true "Raspberry Pi")

This repo demonstates the use of YottaDB as a time series database that is then used to present data to Grafana.

As an example, placing YottaDB in a relevant Internet of Things (IoT) setting, a Raspberry Pi is used and an attached D11 temperature/humidity sensor utilised to read data, and publish the data to an MQTT message broker. Another process then subscribes to the message broker, reading from the message topic before sending the data to Yottadb.

The YottaDB mg-webserver is then used to present data from YottaDB as JSON based API endpoints. These endpoints are then "consumed" by Grafana via the infinity plugin.

![Alt text](yottadb.iot-arch.png?raw=true "Architecture")

# Installation

# Raspberry Pi

You can run this demo without a Raspberry Pi using dummy step. If you don't have a Raspberry Pi or equivalent hardware, skip this step.

Connect the DHT11 (D11) sensor to your Raspberry Pi using the following guide:

https://www.circuitbasics.com/how-to-set-up-the-dht11-humidity-sensor-on-the-raspberry-pi/

Install git:

   sudo apt-get update
   sudo apt-get install -y git

Clone the repo:

    cd /usr/local
    git clone https://github.com/RamSailopal/YottaDB-IoT.git
   
Install the neccesary packages for the sensor:

    cd /usr/local/YottaDB-IoT
    sudo ./installpi.sh
    
 # Gitpod
   
1) Create a free/paid Gitpod account - https://www.gitpod.io/
2) Log into the account
3) Open a new browser tab and add **gitpod.io/#https://github.com/RamSailopal/YottaDB-IoT** to the address - This will create a new Gitpod cloud instance.
4) Let the containers fully load
5) Without a Raspberry Pi, open a new terminal and run:

    python3 mqttsend.py
    
   With a Raspberry Pi, go to your Pi terminal and:
    
    cd /sr/local/YottaDB-IoT
    python3 mqttsendpi.py
    
 6) Open a new tab as below, substituting the unique Gitpod address for the one you are running

 ![Alt text](sensor-glob.JPG?raw=true "Global View")

    
