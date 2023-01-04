import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

led = 11

GPIO.setup(led, GPIO.OUT, initial=GPIO.LOW)
GPIO.output(led,GPIO.HIGH)
time.sleep(5)
