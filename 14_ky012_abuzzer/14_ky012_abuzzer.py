import RPi.GPIO as GPIO
import time


BUZZER_PIN = 7  # Buzzer pin number

GPIO.setmode(GPIO.BOARD)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

print("Active buzzer making 2.5kHz sound for 2 seconds.")

GPIO.output(BUZZER_PIN, GPIO.HIGH)
time.sleep(2)
GPIO.output(BUZZER_PIN, GPIO.LOW)

GPIO.cleanup()  # Clear GPIO
