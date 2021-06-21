import time
import serial


class Serial:
    def __init__(self,serial_port):
        self.serial_port = serial_port

    def send(data, dataLength):
        self.serial_port.write(data)
    
    def receive():
        self.serial_port
