import RPi.GPIO as GPIO


def button_pressed(data):
    data['remaining_clicks'] -= 1
    print("Remaining Clicks: {}".format(data['remaining_clicks']))


BUTTON_PIN = 12  # Set the button pin number into a variable

GPIO.setmode(GPIO.BOARD)  # Set GPIO mode to BOARD to use pin numbers
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Prepare button pin

data = {'remaining_clicks': 5}  # Create a dict because it's mutable

GPIO.add_event_detect(  # Detect button event on rising edge
    BUTTON_PIN, GPIO.RISING,
    callback=lambda x: button_pressed(data),  # Use lambda to pass parameters
    bouncetime=250  # Use bouncetime to avoid extra clicks
)

print("Exit script by pressing the button 5 times.")

while data['remaining_clicks'] > 0:
    pass

GPIO.cleanup()  # Clear GPIO
