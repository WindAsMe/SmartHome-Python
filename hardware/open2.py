# import the GPIO and time package
import RPi.GPIO as GPIO
import time



# Pin  Definitions
ledPin = 11



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
