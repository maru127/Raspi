import RPi.GPIO as GPIO
import time

servo = 12

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(servo, GPIO.OUT, initial=GPIO.LOW)

GPIO.output(servo,GPIO.LOW)

pwm_servo = GPIO.PWM(servo, 50)
pwm_servo.start(0)
print('Wating for 1 sec') 
time.sleep(1)

try:
    pwm_servo.ChangeDutyCycle(0)
    time.sleep(1)
    pwm_servo.ChangeDutyCycle(12)
    time.sleep(1)


finally:
    pwm_servo.ChangeDutyCycle(0)
    pwm_servo.stop()
    print('cleaning up!')
    GPIO.cleanup()