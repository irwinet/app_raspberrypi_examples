import RPi.GPIO as GPIO


def next_rgb_color(r_pin, g_pin, b_pin, data):
    led_colors = [(1, 0, 0), (1, 0, 1), (0, 0, 1),
                  (0, 1, 1), (0, 1, 0), (1, 1, 0)]
    GPIO.output([r_pin, g_pin, b_pin], led_colors[data['index']])
    data['index'] += 1  # Increment index
    if data['index'] >= len(led_colors):  # If index out of range
        data['index'] = 0  # Restart from first color


R_PIN = 11  # Set up Red pin
G_PIN = 13  # Set up Green pin
B_PIN = 15  # Set up Blue pin
BUTTON_PIN = 12  # Set the BUTTON pin number into a variable
data = {'index': 0}  # Create a dict because it's mutable
GPIO.setmode(GPIO.BOARD)  # Set GPIO mode to BOARD to use pin numbers
GPIO.setup(R_PIN, GPIO.OUT, initial=0)  # Prepare Red pin
GPIO.setup(G_PIN, GPIO.OUT, initial=0)  # Prepare Green pin
GPIO.setup(B_PIN, GPIO.OUT, initial=0)  # Prepare Blue pin
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Prepare BUTTON pin

# Use def function to pass parameters
btn_function = lambda x: next_rgb_color(R_PIN, G_PIN, B_PIN, data)

# Setup event on rising edge
GPIO.add_event_detect(BUTTON_PIN, GPIO.RISING,
                      callback=btn_function,
                      bouncetime=300)

raw_input("Exit script by pressing enter")

GPIO.cleanup()  # Clear GPIO
