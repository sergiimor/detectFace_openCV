#import uart
import time
import serial

serial_port = serial.Serial(
    port="/dev/ttyUSB0",
    baudrate=115200,
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
)
time_sleep = 0.5
class Commands:
     
    def openConnection(self, test):
        if test == False:
            serial_port.write("\x80")
            time.sleep(0.5)
        else:
            print('Open connection')
            time.sleep(time_sleep)

    def setFullMode(self, test):
        if test == False:
            serial_port.write("\x83")
            time.sleep(0.3)
        else:
            print('setFullMode')
            time.sleep(0.3)

    def closeConnection(self, test):
        if test == False:
            serial_port.write("\xAD")
            time.sleep(1)
        else:
            print('Close connection')
            time.sleep(1)

    def fordward(self, test):
        if test == False:
            serial_port.write("\x89\x00\x64\x00\x00")
            time.sleep(time_sleep)
        else:
            print('fordward')
            time.sleep(time_sleep)

    def backward(self, test):
        if test == False:
            serial_port.write("\x89\xFF\x9C\x00\x00")
            time.sleep(time_sleep)
        else:
            print('backward')
            time.sleep(time_sleep)

    def left(self, test):
        if test == False:
            serial_port.write("\x89\x00\x40\xFF\x00")
            time.sleep(time_sleep)
        else:
            print('left')
            time.sleep(time_sleep)

    def rigth(self, test):
        if test == False:
            serial_port.write("\x89\x00\x40\x00\xFF")
            time.sleep(time_sleep)
        else:
            print('rigth')
            time.sleep(time_sleep)

    def stop(self, test):
        if test == False:
            serial_port.write("\x89\x00\x00\x00\x00")
            time.sleep(time_sleep)
        else:
            print('stop')
            time.sleep(time_sleep)