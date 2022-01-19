# YottaDB-IoT

![Alt text](raspberrypi.jpg?raw=true "Raspberry Pi")

This repo demonstates the use of YottaDB as a time series database that is then used to present data to Grafana.

As an example, placing YottaDB in a relevant Internet of Things (IoT) setting, a Raspberry Pi is used and an attached D11 temperature/humidity sensor utilised to read data, and publish the data to an MQTT message broker. Another process then subscribes to the message broker, reading from the message topic before sending the data to Yottadb.

The YottaDB mg-webserver is then used to present data from YottaDB as JSON based API endpoints. These endpoints are then "consumed" by Grafana via the infinity plugin.

![Alt text](yottadb-iot-arch.png?raw=true "Architecture")
