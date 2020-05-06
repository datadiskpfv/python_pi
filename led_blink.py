import RPi.GPIO as GPIO
import time

ledPin = 11                             # GPIO 17 (pin 11)


def setup():
    GPIO.setmode(GPIO.BOARD)            # use PHYSICAL GPIO numbering
    GPIO.setup(ledPin, GPIO.OUT)        # set the ledPin to OUTPUT mode
    GPIO.output(ledPin, GPIO.LOW)       # make ledPin output LOW level (turn off)
    print('using ping%d'%ledPin)


def loop():
    while True:
        GPIO.output(ledPin, GPIO.HIGH)  # turn on led
        print('led turned on >>>')
        time.sleep(1)
        GPIO.output(ledPin, GPIO.LOW)   # turn off led
        print('led turned off >>>')
        time.sleep(1)


def destroy():
    GPIO.cleanup()                      # Release all GPIO


if __name__ == '__main__':
    print('Program led blink is starting.... \n')
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()


