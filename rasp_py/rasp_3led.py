import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

led_list=[11,15,13]

GPIO.setup(led_list, GPIO.OUT, initial=GPIO.LOW)
# GPIO.output(led1, GPIO.HIGH)

while True:
    for i in led_list:
        GPIO.output(led_list, GPIO.LOW)
        time.sleep(2)
        GPIO.output(i, GPIO.HIGH)
        time.sleep(2)
        
    # for i in range(3):
            

    #     GPIO.output(led_list[i], GPIO.HIGH)
    #     time.sleep(1)
    #     GPIO.output(led_list, GPIO.LOW)
    #     time.sleep(1)
        