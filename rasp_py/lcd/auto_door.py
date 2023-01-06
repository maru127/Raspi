import RPi.GPIO as GPIO
import I2C_driver as LCD
from time import *

seg = [38, 29, 31, 33, 35, 37, 40]
servo_pin= 12
pin_trig = 13
pin_echo = 11
mylcd = LCD.lcd()

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

def setup():        #핀 설정
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(seg, GPIO.OUT, initial=GPIO.HIGH)

    GPIO.setup(servo_pin, GPIO.OUT)

    GPIO.setup(pin_trig, GPIO.OUT)
    GPIO.setup(pin_echo, GPIO.IN)
    

def cal_angle(input_angle):     #각도를 입력받아 해당하는 듀티비를 리턴
    #input_angle = int(input("0~180"))
    if input_angle >= 180:
        input_angle = 177
    elif input_angle <= 0:
        input_angle = 3
    angle = 10/180*input_angle
    return angle

def cal_us():          #초음파센서이용해서 거리 구하기
    start_time = 0
    stop_time = 0
    GPIO.output(pin_trig, False)
    sleep(1)

    #print('cal dis')
    GPIO.output(pin_trig, True)
    sleep(0.000001)
    GPIO.output(pin_trig, False)

    while GPIO.input(pin_echo) == 0:
        start_time = time()
    while GPIO.input(pin_echo) == 1:
        stop_time = time()
    
    time_inter = stop_time - start_time
    dis = time_inter * 17000
    dis = round(dis, 2)
    # print('dis => ', dis, 'cm')
    mylcd.lcd_display_string(str(dis)+"cm                ",1)
    return dis

def move_servo(angle):      #서보모터 조정
    GPIO.output(servo_pin,GPIO.LOW)

    pwm_servo = GPIO.PWM(servo_pin, 50)
    pwm_servo.start(0)  
    #print('Wating for 1 sec') 
    #sleep(1)
    
    GPIO.setup(servo_pin, GPIO.OUT)     #70, 72, 73 서보모터 지터 방지코드
    pwm_servo.ChangeDutyCycle(angle)    
    sleep(0.3)
    GPIO.setup(servo_pin, GPIO.IN)
    sleep(0.7)
    #pwm_servo.ChangeDutyCycle(0)
    #pwm_servo.stop()

def main():
    setup()        
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin_trig, GPIO.OUT)
    GPIO.setup(pin_echo, GPIO.IN)
    #print("open")
    #move_servo(11)
    #sleep(3)
    #print("close")
    #move_servo(1)
    #sleep(2)

    while True:
        print(cal_us())
        if cal_us() <= 3:
            print('open door')
            move_servo(10)
            GPIO.setup(servo_pin, GPIO.OUT) 
            for i in reversed(range(4)):
                print(i)
                GPIO.output(seg,fnd[i])
                sleep(1)
                
                
            print("close door")
            move_servo(1)
            GPIO.setup(servo_pin, GPIO.OUT) 
            sleep(2)
            




    
    GPIO.cleanup()

if __name__ == '__main__':
    main()