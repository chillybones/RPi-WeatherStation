import Adafruit_DHT
from time import sleep

sensor = Adafruit_DHT.DHT11

pin = 21


while True:
    humid, temp = Adafruit_DHT.read_retry(sensor, pin)
    print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temp, humid))
    sleep(1)