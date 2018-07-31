# import the GPIO and time package
import RPi.GPIO as GPIO


# Pin  Definitions
ledPin = 7


# Pin Setup
GPIO.setmode(GPIO.BOARD)
GPIO.setup(ledPin, GPIO.OUT)

ledStatus = False
GPIO.output(ledPin, ledStatus)

try:
    while False:
        GPIO.output(ledPin, ledStatus)
except KeyboardInterrupt:
    GPIO.cleanup()
    print("Program terminated!")
