import RPi.GPIO as GPIO
import time

LED_PIN = 11  # Set LED_PIN variable to 11

GPIO.setmode(GPIO.BOARD)  # Set GPIO mode to BOARD to use pin numbers
GPIO.setup(LED_PIN, GPIO.OUT)  # Prepare the LED pin to be used

for i in range(3):  # Turn ON and OFF the LED 3 times.
    GPIO.output(LED_PIN, GPIO.HIGH)  # Set LED pin on
    time.sleep(0.5)
    GPIO.output(LED_PIN, GPIO.LOW)  # Set LED pin off
    time.sleep(0.5)

GPIO.cleanup()  # Clear GPIO
