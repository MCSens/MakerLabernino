import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(10, GPIO.IN)
GPIO.setup(3, GPIO.OUT)

i_old = GPIO.input(10)
try:
        while True:
                i=GPIO.input(10)
                if(i_old != i):
                        print "Status geaendert"
                        if i==0:                 #When output from motion sensor is LOW
                                print "No intruders",i
                                GPIO.output(3, GPIO.LOW)
                        elif i==1:               #When output from motion sensor is HIGH
                                print "Intruder detected",i
                                GPIO.output(3,GPIO.HIGH)
                        i_old = i
                time.sleep(0.2)
except:
        print "fuck"
        GPIO.output(3, GPIO.LOW)




