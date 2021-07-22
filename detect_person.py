import jetson.inference
import jetson.utils
import command
import time
import sys


#his variable is used for Command class
#True to test the commands
#False to communicate with the serial port
test = True

#Command class is used for the serial port communication
command1 = command.Commands()
command1.openConnection(test)
command1.setFullMode(test)

start_time = time.time()


#Load the pretrained facenet model. Use default threshols value.
 
net = jetson.inference.detectNet("facenet", threshold = 0.5)

#Using CSI camera with resolution of 640x480 pixels
camera =  jetson.utils.gstCamera(640, 480, "csi://0")
#camera =  jetson.utils.gstCamera(1920, 1080, "csi://0")
#camera =  jetson.utils.gstCamera(640, 480, "/dev/video1")

'''
Display the image and the position of the pixels
(0,0)	      (640,0)
x-----------------x
|		  |
|		  |
|		  |
|		  |
x-----------------x
(0,480)		(640,480)		

'''
display = jetson.utils.glDisplay()

def controlActuator (x1, y1): 

	#if the x coordinate is higher than 360 the robot turn clock wise
	if x1 > 360:
		command1.clkwise(test)
	#if the x coordinate is lower than 260 the robot turn counter clock wise
	elif x1 < 260:
		command1.counter_clkwise(test)
	#if the y coordinate is lower than 210 the robot move backward	
	elif y1 < 210:
		command1.backward(test)
	#if the y coordinate is higher than 270 the robot move fordward
	elif  y1 > 270:
		command1.fordward(test)
	else:
		command1.stop(test)

while True:

	#Takes the raw format of the camera and converts it into floating-point rgba on the GPU
	img , width, height = camera.CaptureRGBA()
	#Performs the detection of the image converted and returns a list containing the detected object
	detection = net.Detect(img , width, height)

	if detection:
		#if a face is detected refresh the value of the time
		start_time = time.time()
		x, y = detection[0].Center
		w = detection[0].Width
		h = detection[0].Height
		print('El centre de les x es: ' + str(x))
		print('El centre de les y es: ' + str(y))
		
		#Set the value of x and y coordinates in order to control the robot
		controlActuator(x, y)
	else:
		#If a face is not detected during more than 2 seconds the robot will start turning counter clock wise
		if (time.time() - start_time > 2):
			controlActuator(100, 240)
		#These coordinates correspond to the center of the box so the robot will stop
		controlActuator(320, 240)
	#Render a CUDA float4 image using OpenGL interop to the windows
	display.RenderOnce(img , width, height)
	#Setting the title
	display.SetTitle( "Object detection | Network {:.0f} FPS".format(net.GetNetworkFPS()))

#Close connection and close camera
print ('close connection')
command1.closeConnection(test)
camera.Close()
exit()

