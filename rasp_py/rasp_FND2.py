import RPi.GPIO as GPIO
import time

#      A   B   C   D   E   F   G
seg = [27, 29, 31, 33, 35, 37, 40]

fnd  = [(1,1,1,1,1,1,0),    #0
        (1,0,0,1,1,1,1),    #1
        (0,0,1,0,0,1,0),    #2
        (0,0,0,0,1,1,0),    #3
        (1,0,0,1,1,0,0),    #4
        (0,1,0,0,1,0,0),    #5
        (0,1,0,0,0,0,0),    #6
        (0,0,0,1,1,0,1),    #7
        (0,0,0,0,0,0,0),    #8
        (0,0,0,0,1,0,0)]    #9


GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(seg, GPIO.OUT, initial=GPIO.LOW)

try:
    while True:
        i = int(input("0 ~ 9 : "))
        GPIO.output(seg, fnd[i])

finally:
    print('cleaning up!')