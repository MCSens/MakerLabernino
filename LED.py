import RPi.GPIO as GPIO
import time
                                                      
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(12, GPIO.OUT)
print("LED ROT AN")
GPIO.output(12,GPIO.HIGH)
time.sleep(2)
GPIO.output(12, GPIO.LOW)

GPIO.setup(13, GPIO.OUT)
print("LED GELB AN")
GPIO.output(13,GPIO.HIGH)
time.sleep(1)
GPIO.output(13, GPIO.LOW)

GPIO.setup(15, GPIO.OUT)
print("LED GRÜN AN")
GPIO.output(15,GPIO.HIGH)
time.sleep(1)
GPIO.output(15, GPIO.LOW)

