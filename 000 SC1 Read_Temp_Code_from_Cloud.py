import pymssql
import time
import RPi.GPIO as GPIO

  
deviceid = "raspberry_python"
conn = pymssql.connect(server='iotmakerlab.database.windows.net', user='ITIM@iotmakerlab', password='Mobility4zf', database='IoT-Makerlab-DB')
cursor = conn.cursor()
stmt = 'SELECT top 1 * FROM dbo.IML_TEMP ORDER BY TIMESTAMP DESC;'
#stmt = 'SELECT * FROM dbo.IML_TEMP ORDER BY TIMESTAMP DESC;'
cursor.execute(stmt)
row = cursor.fetchone()

def switch_led(temp):
    GPIO.setwarnings(False)
    GPIO.cleanup()
    GPIO.setmode(GPIO.BOARD)

    if temp < 25:
        pin = 15 #color green
    elif temp < 27:
        pin = 13
    else:
        pin = 12

    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin,GPIO.HIGH)

while True:
    try:
        print str(row[0]) + " | " + str(row[1]) + " | " + str(row[2]) + " | " + str(row[3])
        temp = row[2]

        switch_led(temp)
        cursor = conn.cursor()
        cursor.execute(stmt)
        row = cursor.fetchone()
    except:
        print("fuckuphappened")
        GPIO.cleanup()
        exit()


