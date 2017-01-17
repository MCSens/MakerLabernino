import pymssql
import time

deviceid = "raspberry_python"
conn = pymssql.connect(server='iotmakerlab.database.windows.net', user='ITIM@iotmakerlab', password='Mobility4zf', database='IoT-Makerlab-DB')
cursor = conn.cursor()
stmt = 'SELECT top 1 * FROM dbo.IML_TEMP ORDER BY TIMESTAMP DESC;'
cursor.execute(stmt)
row = cursor.fetchone()
while True:
    print str(row[0]) + " " + str(row[1]) + " " + str(row[2])
    cursor.execute(stmt)
    row = cursor.fetchone()
    time.sleep(5)

