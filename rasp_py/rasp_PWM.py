import RPi.GPIO as GPIO

LED = 12

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)

GPIO.output(LED,GPIO.LOW)

pwm_led = GPIO.PWM(LED, 100)
pwm_led.start(0)

try:
    while True:
        duty_led = input('0 ~ 100 : ')
        duty = int(duty_led)
        print('duty rate = ', duty)
        pwm_led.ChangeDutyCycle(duty)

finally:
    pwm_led.stop()
    print('cleaning up!')
    GPIO.cleanup()