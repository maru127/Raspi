import RPi.GPIO as GPIO
import time

#      A   B   C   D   E   F   G
seg = [38, 29, 31, 33, 35, 37, 40]

fnd  = [(0,0,0,0,0,0,1),    #0
        (1,0,0,1,1,1,1),    #1
        (0,0,1,0,0,1,0),    #2
        (0,0,0,0,1,1,0),    #3
        (1,0,0,1,1,0,0),    #4
        (0,1,0,0,1,0,0),    #5
        (0,1,0,0,0,0,0),    #6
        (0,0,0,1,1,0,1),    #7
        (0,0,0,0,0,0,0),    #8
        (0,0,0,0,1,0,0)]    #9

num = 0

def FND_setup():
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        GPIO.setup(seg, GPIO.OUT, initial=GPIO.HIGH)

def main():
        i=0
        FND_setup()
        GPIO.output(seg,GPIO.HIGH)

        while True:
                j = int(input())
                GPIO.output(seg,fnd[j])
        
if __name__ == '__main__':
        main()
