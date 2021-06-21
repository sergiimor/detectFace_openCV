import serial
import time 
serial_port = serial.Serial(
    port="/dev/ttyUSB0",
    baudrate=115200,
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
)


class Commands:
     
    def openConnection(self):
        serial_port.write("\x80")
        time.sleep(0.1)

    def setFullMode(self):
        serial_port.write("\x83")
        time.sleep(0.1)

    def closeConnection(self):
        serial_port.write("\xAD")
        time.sleep(0.1)

    def fordward(self):
        serial_port.write("\x89\x00\x64\x00\x00")
        time.sleep(0.3)

    def backward(self):
        serial_port.write("\x89\xFF\x9C\x00\x00")
        time.sleep(0.3)

    def left(self):
        serial_port.write("\x89\x00\x40\xFF\x00")
        time.sleep(0.3)
    def rigth(self):
        serial_port.write("\x89\x00\x40\x00\xFF")
        time.sleep(0.3)
    
    def stop(self):
        serial_port.write("\x89\x00\x00\x00\x00")
        time.sleep(0.3)

command1 = Commands()
command1.openConnection()
command1.setFullMode()
print("Set communication with roomba")

command1.fordward()

command1.left()
command1.left()
command1.left()
command1.stop()
command1.stop()
command1.backward()
command1.backward()
command1.backward()
command1.backward()

command1.stop()

print("Set communication with roomba")


