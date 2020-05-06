import RPi.GPIO as GPIO

ledPin = 11                             # GPIO 17 (pin 11)
buttonPin = 12                          # GPIO 18 (pin 12)

# PULL UP a port means - 3.3v, HIGH, True    (GPIO pins are 3.3 volts)
# PULL DOWN a port means - 0v, LOW, FALSE
def setup():
    GPIO.setmode(GPIO.BOARD)            # use PHYSICAL GPIO numbering
    GPIO.setup(ledPin, GPIO.OUT)        # set the ledPin to OUTPUT mode
    GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)       # set buttonPin to PULL UP INPUT mode


def loop():
    while True:
        if GPIO.input(buttonPin) == GPIO.LOW:       # will be either LOW or HIGH
            GPIO.output(ledPin, GPIO.HIGH)
            print("led turned on >>>")
        else:
            GPIO.output(ledPin, GPIO.LOW)
            print("led turned off >>>")


def destroy():
    GPIO.cleanup()                      # Release all GPIO


if __name__ == '__main__':
    print('Program led button is starting.... \n')
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()