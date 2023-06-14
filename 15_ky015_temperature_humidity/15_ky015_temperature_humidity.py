import Adafruit_DHT
import RPi.GPIO as GPIO
import time


DHTSensor = Adafruit_DHT.DHT11
KY015 = 4

print("Use CTRL+C to exit.")

try:
    while True:
        h, t = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, KY015)
        print("Temperature {}C     Humidity {}%".format(t, h))
        time.sleep(1.5)
except Exception as e:
    GPIO.cleanup()
