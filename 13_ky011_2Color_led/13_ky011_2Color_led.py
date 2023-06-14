import RPi.GPIO as GPIO
import time


def fade_blink(pin, reverse=False):
    _range = range(100, -1, -1) if reverse else range(1, 100)

    for i in _range:
        pin.ChangeDutyCycle(i)
        time.sleep(0.005)


R_PIN = 11
G_PIN = 13

GPIO.setmode(GPIO.BOARD)  # Set GPIO mode to BOARD to use pin numbers
GPIO.setup([R_PIN, G_PIN], GPIO.OUT)  # Prepare the color pins

red_pin = GPIO.PWM(R_PIN, 2000)  # set Frequece to 2KHz
green_pin = GPIO.PWM(G_PIN, 2000)

red_pin.start(0)
green_pin.start(0)

# Set red intensity from 1 to 100 and from 100 to 0
fade_blink(red_pin)
fade_blink(red_pin, reverse=True)
time.sleep(0.5)

# Set green intensity from 1 to 100 and from 100 to 0
fade_blink(green_pin)
fade_blink(green_pin, reverse=True)
time.sleep(0.5)

# Make both green and red at the same time
red_pin.ChangeDutyCycle(10)
green_pin.ChangeDutyCycle(100)
time.sleep(0.5)

GPIO.cleanup()  # Clear GPIO


