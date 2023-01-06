import RPi.GPIO as GPIO
import time

def main():
    pin_trig = 13
    pin_echo = 11
    
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin_trig, GPIO.OUT)
    GPIO.setup(pin_echo, GPIO.IN)

    start_time = 0
    stop_time = 0
    
    while True:
        GPIO.output(pin_trig, False)
        time.sleep(1)

        print('cal dis')
        GPIO.output(pin_trig, True)
        time.sleep(0.000001)
        GPIO.output(pin_trig, False)

        while GPIO.input(pin_echo) == 0:
            start_time = time.time()
        while GPIO.input(pin_echo) == 1:
            stop_time = time.time()
        
        time_inter = stop_time - start_time
        dis = time_inter * 17000
        dis = round(dis, 2)

        print('dis => ', dis, 'cm')
    GPIO.cleanup()

if __name__ == '__main__':
    main()