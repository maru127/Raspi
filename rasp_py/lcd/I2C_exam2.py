import I2C_driver as LCD
from time import *
mylcd = LCD.lcd()
mylcd.lcd_display_string("Hello World",1)
mylcd.lcd_display_string("Raspberry Pi3 b+",2)
sleep(5)

mylcd.lcd_clear()
mylcd.lcd_display_string("LCD display",2)

try:
    while True:
        c = input()
        
        mylcd.lcd_display_string(c,1)

finally:
    print('cleaning up!')
