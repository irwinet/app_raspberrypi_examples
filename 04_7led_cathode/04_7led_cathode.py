import RPi.GPIO as GPIO
import time


# Segments:  a  b   c   d   e   f   g
PINS_LIST = [8, 11, 12, 13, 15, 16, 18]

GPIO.setmode(GPIO.BOARD)  # Set GPIO mode to BOARD to use pin numbers
GPIO.setup(PINS_LIST, GPIO.OUT, initial=GPIO.LOW)  # Prepare all pins

char_dict = {
    0: (1, 1, 1, 1, 1, 1, 0),  # 0
    1: (0, 1, 1, 0, 0, 0, 0),  # 1
    2: (1, 1, 0, 1, 1, 0, 1),  # 2
    3: (1, 1, 1, 1, 0, 0, 1),  # 3
    4: (0, 1, 1, 0, 0, 1, 1),  # 4
    5: (1, 0, 1, 1, 0, 1, 1),  # 5
    6: (1, 0, 1, 1, 1, 1, 1),  # 6
    7: (1, 1, 1, 0, 0, 0, 0),  # 7
    8: (1, 1, 1, 1, 1, 1, 1),  # 8
    9: (1, 1, 1, 1, 0, 1, 1),  # 9
    'a': (1, 1, 1, 0, 1, 1, 1),  # A
    'c': (1, 0, 0, 1, 1, 1, 0),  # C
    'd': (0, 1, 1, 1, 1, 0, 1),  # d
    'e': (1, 0, 0, 1, 1, 1, 1),  # E
    'f': (1, 0, 0, 0, 1, 1, 1),  # F
    'h': (0, 1, 1, 0, 1, 1, 1),  # H
    'p': (1, 1, 0, 0, 1, 1, 1),  # P
    'u': (0, 1, 1, 1, 1, 1, 0),  # U
}

for key, value in sorted(char_dict.items()):
    GPIO.output(PINS_LIST, value)
    time.sleep(1)

GPIO.cleanup()  # Clear GPIO
