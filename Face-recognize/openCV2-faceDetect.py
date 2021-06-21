import cv2 as cv
import numpy as np
import command

focal_distance = 150

def measure_distance(width):
    return ((30*focal_distance)/width)

def distance_to_camera (knowWidth, focalLength, perWidth):
    return (knowWidth * focalLength)/perWidth

KNOWN_DISTANCE = 2

KNOWN_WIDTH = 1

dispW=640
dispH=480
flip=2
x1 = 0
y = 0
test = 0
countDistance = 0

cam=cv.VideoCapture(0)
width = cam.get(cv.CAP_PROP_FRAME_WIDTH)
height = cam.get(cv.CAP_PROP_FRAME_HEIGHT)
print ('width: ', width, 'height: ', height)

command1 = command.Commands()
command1.openConnection(test)
command1.setFullMode(test)

face_cascade = cv.CascadeClassifier('/home/sergi/Desktop/Face-recognize/gitrepo/cascade/face.xml')
while True:

    ret, frame  = cam.read()

    frame = cv.resize(frame, (640, 480))
    #Ens tornara de color gris les cares
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY )
    #El model que volem entrenar
    #Each array will have the x and the y of the corner of the box like a box around my face it would be the x and the y, the width and the heigth
    #Face returns four numbers, of an array of an array X Y WH, X Y WH, X Y WH..
    faces=face_cascade.detectMultiScale(gray, 1.1,4)
    for(x,y,w,h) in faces:
        cv.rectangle(frame, (x, y), (x+w, y+h), (0,0,255), 2)

        if faces.any:
            print('face detect')
            objX = x+w/2
            objY = y+h/2

            errorX = objX - width/2
            errorY = objY - height/2

            if errorX > 64:
                x1 = x1 - 1
            if errorX < -64:
                x1 = x1 + 1
            if errorY > 0:
                y = y - 1
            if errorY < 0:
                y = y + 1  
            print(x1)
            if x1 > 0:
                print('Vaig a la dreta')
                command1.rigth(test)
                x1 = 0
                print(x1)

            if x1 < 0:
                print('Vaig a lesquerra')
                command1.left(test)
                x1 = 0 

            distance = measure_distance(w)
            print(distance)
            if distance > 110:
                print('Distancia mes de un metre')
                countDistance = countDistance + 1
                if countDistance > 2:
                    countDistance = 0
                    command1.fordward(test)
            elif distance < 90:
                print('Distancia menor de un metre')
                countDistance = countDistance - 1
                if countDistance < -2:
                    countDistance = 0
                    command1.backward(test)
            else:
                print('Parat')
                command1.stop(test)
            print(faces)
        else:
            print('stop')
            command1.stop(test)

    cv.imshow('nanoCam',frame)
    cv.moveWindow('nanoCam', 0,0)
    if cv.waitKey(1)==ord('q'):
        break
command1.closeConnection(test)
cam.release()
cv.destroyAllWindows()