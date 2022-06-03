import serial
import time
com_serial=serial.Serial('COM2',9600, timeout=0)

while True:
    print(com_serial.readline())
    com_serial.write(b'hola mundo\n\r')
    time.sleep(1)
    


