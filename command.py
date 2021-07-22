import time
import serial

#Configure the parameters of the Port serial
serial_port = serial.Serial(
    port="/dev/ttyUSB0",
    baudrate=115200,
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
)

time_sleep = 0.2

class Commands:
     
    def openConnection(self, test):
        if test == False:
            serial_port.write("\x80")
            time.sleep(0.1)
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

    def fordward(self, 	test):
        if test == False:
            serial_port.write("\x89\x00\x30\x00\x00")
            time.sleep(time_sleep)
        else:
            print('fordward')
            time.sleep(time_sleep)

    def backward(self, test):
        if test == False:
            serial_port.write("\x89\xFF\xD0\x00\x00")
            time.sleep(time_sleep)
        else:
            print('backward')
            time.sleep(time_sleep)

    def counter_clkwise(self, test):
        if test == False:
            serial_port.write("\x89\x00\x20\x00\x01")
            time.sleep(time_sleep)
        else:
            print('counter_clkwise')
            time.sleep(time_sleep)

    def clkwise(self, test):
        if test == False:
            serial_port.write("\x89\x00\x10\xFF\xFF")
            time.sleep(time_sleep)
        else:
            print('clkwise')
            time.sleep(time_sleep)

    def stop(self, test):
        if test == False:
            serial_port.write("\x89\x00\x00\x00\x00")
            time.sleep(time_sleep)
        else:
            print('stop')
            time.sleep(time_sleep)
