# Import libraries
import RPi.GPIO as GPIO
import time
import Adafruit_SSD1306

from PIL import Image
# Set GPIO numbering mode
GPIO.setmode(GPIO.BCM)

## 128x64 display with hardware I2C:
disp = Adafruit_SSD1306.SSD1306_128_64(rst=None)

# Set pins 12 & 11 (18 & 17 BCM) as outputs, and define as PWM servo1 & servo2
GPIO.setup(18,GPIO.OUT)
displayArm = GPIO.PWM(18,50) # pin 11 for display arm
GPIO.setup(17,GPIO.OUT)
switchArm = GPIO.PWM(17,50) # pin 12 for switch arm 

# Set pin 18 (24 BCM) input for switch
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP) 

## Initialize Oled library.
disp.begin()
#
## Clear display.
disp.clear()
disp.display()

# Start PWM running on both servos, value of 0 (pulse off)
displayArm.start(0)
switchArm.start(0)

#Reset Switch arm
switchArm.ChangeDutyCycle(2+(0/18))
time.sleep(0.7)
switchArm.ChangeDutyCycle(0)

#Reset Display arm
displayArm.ChangeDutyCycle(2+(85/18))
time.sleep(0.5)
displayArm.ChangeDutyCycle(0)

while True:
    
    while GPIO.input(24) == GPIO.HIGH:
        time.sleep(0.01)  # wait 10 ms to give CPU chance to do other things
        image = Image.open('face.ppm').convert('1')
        disp.image(image)
        disp.display()
        time.sleep(1)
        
        print("Switch Has Been Flipped!")
        time.sleep(0.5)
        switchArm.ChangeDutyCycle(2+(20/18))
        time.sleep(0.5)
        switchArm.ChangeDutyCycle(0)
        
        displayArm.ChangeDutyCycle(2+(18/18))
        time.sleep(0.4)
        displayArm.ChangeDutyCycle(0)
        time.sleep(0.5)
        image = Image.open('fuck.ppm').convert('1')
        disp.image(image)
        disp.display()
        time.sleep(1.5)
        displayArm.ChangeDutyCycle(2+(85/18))
        time.sleep(0.5)
        displayArm.ChangeDutyCycle(0)
        disp.clear()
        disp.display()
        
        switchArm.ChangeDutyCycle(2+(145/18))
        time.sleep(0.7)
        
        if GPIO.input(24) == GPIO.LOW:
                print("Switch Has Been Turned Off!")
                switchArm.ChangeDutyCycle(2+(0/18))
                time.sleep(0.7)
                switchArm.ChangeDutyCycle(0)
        else:
                print("WHAT!!! HOW?")
                while GPIO.input(24) != GPIO.LOW:
                        switchArm.ChangeDutyCycle(2+(70/18))
                        time.sleep(2.7)
                        switchArm.ChangeDutyCycle(2+(145/18))
                        time.sleep(2)
                switchArm.ChangeDutyCycle(2+(0/18))
                time.sleep(0.7)
                switchArm.ChangeDutyCycle(0)
    
time.sleep(0.3)