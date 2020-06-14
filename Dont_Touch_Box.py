# Import libraries
import RPi.GPIO as GPIO
import time
import Adafruit_SSD1306

from PIL import Image
# Set GPIO numbering mode
GPIO.setmode(GPIO.BOARD)


## 128x64 display with hardware I2C:
#disp = Adafruit_SSD1306.SSD1306_128_64(rst=24)


# Set pins 11 & 12 as outputs, and define as PWM servo1 & servo2
GPIO.setup(12,GPIO.OUT)
displayArm = GPIO.PWM(12,50) # pin 11 for display arm
GPIO.setup(11,GPIO.OUT)
switchArm = GPIO.PWM(11,50) # pin 12 for switch arm 

# Set pin 18 input for switch
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP) 

## Initialize Oled library.
#disp.begin()
#
## Clear display.
#disp.clear()
#disp.display()

# Start PWM running on both servos, value of 0 (pulse off)
displayArm.start(0)
switchArm.start(0)

while True:
    
    while GPIO.input(18) == GPIO.HIGH:
        time.sleep(0.01)  # wait 10 ms to give CPU chance to do other things
        
        print("Switch Has Been Flipped!")
        time.sleep(0.5)
        switchArm.ChangeDutyCycle(2+(20/18))
        time.sleep(0.5)
        switchArm.ChangeDutyCycle(0)
        
        displayArm.ChangeDutyCycle(2+(30/18))
        time.sleep(0.2)
        displayArm.ChangeDutyCycle(0)
        time.sleep(0.7)
        displayArm.ChangeDutyCycle(2+(70/18))
        time.sleep(0.2)
        displayArm.ChangeDutyCycle(0)
        switchArm.ChangeDutyCycle(2+(145/18))
        time.sleep(0.7)
    
        print("Switch Has Been Turned Off!")
        switchArm.ChangeDutyCycle(2+(0/18))
        time.sleep(0.7)
        switchArm.ChangeDutyCycle(0)
        displayArm.ChangeDutyCycle(2+(70/18))
        time.sleep(0.5)
        displayArm.ChangeDutyCycle(0)
    
time.sleep(0.3)