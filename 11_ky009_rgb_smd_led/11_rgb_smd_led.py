import RPi.GPIO as GPIO
import time


def fade_blink(pin, pin_val, reverse=False):
    if not pin_val:
        return

    _range = range(100, 1, -1) if reverse else range(1, 100)

    for i in _range:
        pin.ChangeDutyCycle(i)
        time.sleep(0.005)


G_PIN = 7
R_PIN = 11
B_PIN = 13

GPIO.setmode(GPIO.BOARD)  # Set GPIO mode to BOARD to use pin numbers
GPIO.setup([R_PIN, G_PIN, B_PIN], GPIO.OUT)  # Prepare the color pins

red_pin = GPIO.PWM(R_PIN, 2000)  # set Frequece to 2KHz
green_pin = GPIO.PWM(G_PIN, 2000)
blue_pin = GPIO.PWM(B_PIN, 2000)

red_pin.start(0)
green_pin.start(0)
blue_pin.start(0)

string_colors = ['Red', 'Magenta', 'Blue', 'Cyan', 'Green', 'Yellow']
led_colors = [(1, 0, 0), (1, 0, 1), (0, 0, 1), (0, 1, 1), (0, 1, 0), (1, 1, 0)]

for color_tuple in led_colors:  # Iterate over the led_colors array
    green_pin.ChangeDutyCycle(color_tuple[1])
    red_pin.ChangeDutyCycle(color_tuple[0])
    blue_pin.ChangeDutyCycle(color_tuple[2])

    index = led_colors.index(color_tuple)  # Get the index to print color name
    print("Color: {}".format(string_colors[index]))  # Print current color name

    # Change intensity from 1 to 100
    fade_blink(red_pin, color_tuple[0])
    fade_blink(green_pin, color_tuple[1])
    fade_blink(blue_pin, color_tuple[2])

    # Change intensity from 100 to 0
    fade_blink(red_pin, color_tuple[0], reverse=True)
    fade_blink(green_pin, color_tuple[1], reverse=True)
    fade_blink(blue_pin, color_tuple[2], reverse=True)

    time.sleep(1)  # Wait 1 second

GPIO.cleanup()  # Clear GPIO
