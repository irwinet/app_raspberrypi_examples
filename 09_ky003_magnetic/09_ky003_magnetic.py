import RPi.GPIO as GPIO
import time


KY003 = 7
LED = 11


def toggle_led(null):  # Function to toggle LED on/off when signal detected
    if GPIO.input(LED):
        GPIO.output(LED, GPIO.LOW)  # If LED is on, turn it off
    else:
        GPIO.output(LED, GPIO.HIGH)  # If LED is off, turn it on


GPIO.setmode(GPIO.BOARD)
GPIO.setup(KY003, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED, GPIO.OUT)

# When a magnetic field is detected toggle_led function will be activated.
GPIO.add_event_detect(KY003, GPIO.FALLING, callback=toggle_led, bouncetime=100)

print("Use CTRL+C to exit.")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()


