from facenet_pytorch import MTCNN
import torch
import numpy as numpy
import cv2 as cv2

#determine device 
device = torch.device('cuda')

#determine MTCNN module
mtcnn = MTCNN(keep_all = True, device = device)

#get sample video from webcam
cam = cv.VideoCapture(0)

#get sample video from CSI camera
cam = cv.VideoCapture("nvcamerasrc ! video/x-raw(memory:NVMM), width=(int)640, height=(int)480, format=(string)I420, framerate=(fraction)30/1 ! nvvidconv flip-method=2 ! video/x-raw, format=(string)I420 ! videoconvert ! video/x-raw, format=(string)BGR ! appsink");
width = cam.get(cv.CAP_PROP_FRAME_WIDTH)
height = cam.get(cv.CAP_PROP_FRAME_HEIGHT)
print ('width: ', width, 'height: ', height)

while True:

	ret, fram = cam.read()

	#VGGFace2 is trained to 160x160px images
	frame_resized = cv.resize(frame, (160, 160))

	frames_tracked = []

	for i, frame_resized in enumerate(frames):
		#detect faces
		boxes, _ = mtcnn.detect(frame_resized)
		frame_draw = frame_resized.copy
		draw = ImageDraw.Draw(frame_draw)
		for box in boxes:
			draw.rectangle(box.tolist(), outline=(255, 0, 0), width=6)

	  	# Add to frame list
		frames_tracked.append(frame_draw.resize((640, 360), Image.BILINEAR))


    cv.imshow('nanoCam',frame)
    cv.moveWindow('nanoCam', 0,0)
    if cv.waitKey(1)==ord('q'):
        break

cam.release()
cv.destroyAllWindows()