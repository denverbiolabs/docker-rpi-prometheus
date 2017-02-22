from prometheus_client import start_http_server, Gauge
import random
import time
import os


ds18b20 = ''

def setup():
    global ds18b20
    for i in os.listdir('/sys/bus/w1/devices'):
        if i != 'w1_bus_master1':
            ds18b20 = i

def read():
    global ds18b20
    location = '/sys/bus/w1/devices/' + ds18b20 + '/w1_slave'
    tfile = open(location)
    text = tfile.read()
    tfile.close()
    secondline = text.split("\n")[1]
    temperaturedata = secondline.split(" ")[9]
    temperature = float(temperaturedata[2:])
    temperature = temperature / 1000
    return temperature
        
def loop():
    while True:
        if read() != None:
            temp = read()
            handle_temp(temp)
            print "Current temperature : %0.3f C" % temp

def destroy():
    pass


# Create a metric to track time spent and requests made.
g = Gauge('fridge_temperature', 'Temperature of the fridge')


def handle_temp(t):
    g.set(t)

if __name__ == '__main__':
    try:
        start_http_server(8000)
        setup()
        loop()
    except KeyboardInterrupt:
        destroy()

