import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
PIR_PIN = 21
GPIO.setup(PIR_PIN, GPIO.IN)
while True:
        i=GPIO.input(PIR_PIN)
        if i==0:
                print ("no motion")
                time.sleep(10)
        elif i==1:
                print ("motion!!!")
                time.sleep(10)
