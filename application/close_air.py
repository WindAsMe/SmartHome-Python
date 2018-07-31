# import the GPIO and time package
import RPi.GPIO as GPIO


def air_close():
    # Pin  Definitions
    led_pin = 7

    # Pin Setup
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(led_pin, GPIO.OUT)

    try:
        for i in range(50):
            GPIO.output(led_pin, True)
    except KeyboardInterrupt:
        GPIO.cleanup()
        print("Program terminated!")

