# import the GPIO and time package
import RPi.GPIO as GPIO



# Pin  Definitions
ledPin = 11



# Pin Setup
GPIO.setmode(GPIO.BOARD)
GPIO.setup(ledPin, GPIO.OUT)

try:
    for i in range(50):                
        GPIO.output(ledPin, True)

except KeyboardInterrupt:
    GPIO.cleanup()
    print("Program terminated!")

