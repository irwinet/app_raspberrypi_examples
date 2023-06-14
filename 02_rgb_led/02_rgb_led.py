import RPi.GPIO as GPIO
import time

R_PIN = 11  # Set up Red pin
G_PIN = 13  # Set up Green pin
B_PIN = 15  # Set up Blue pin

GPIO.setmode(GPIO.BOARD)  # Set GPIO mode to BOARD to use pin numbers
GPIO.setup(R_PIN, GPIO.OUT)  # Prepare the Red pin to be used
GPIO.setup(G_PIN, GPIO.OUT)  # Prepare the Green pin to be used
GPIO.setup(B_PIN, GPIO.OUT)  # Prepare the Blue pin to be used

string_colors = ['Red', 'Magenta', 'Blue', 'Cyan', 'Green', 'Yellow']
led_colors = [(1, 0, 0), (1, 0, 1), (0, 0, 1), (0, 1, 1), (0, 1, 0), (1, 1, 0)]

for color_tuple in led_colors:  # Iterate over the led_colors array
    # Turn Red, Green & Blue pin on/off based on the color tuple
    GPIO.output([R_PIN, G_PIN, B_PIN], color_tuple)
    index = led_colors.index(color_tuple)  # Get the index to print color name
    print("Color: {}".format(string_colors[index]))  # Print current color name
    time.sleep(1.5)  # Wait 1.5 seconds

GPIO.cleanup()  # Clear GPIO
