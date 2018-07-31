# import the GPIO and time package
import RPi.GPIO as GPIO


def light_open():
    # Pin  Definitions
    led_pin = 11

    # Pin Setup
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(led_pin, GPIO.OUT)

    led_status = False
    GPIO.output(led_pin, led_status)

    try:
        while False:
            GPIO.output(led_pin, led_status)
    except KeyboardInterrupt:
        GPIO.cleanup()
        print("Program terminated!")
