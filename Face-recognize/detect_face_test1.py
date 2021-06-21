import cv2 as cv

cam=cv.VideoCapture(0)

face_cascade = cv.CascadeClassifier('/home/sergi/Desktop/Face-recognize/gitrepo/cascade/face.xml')

while True:

    ret, frame  = cam.read()

    #frame = cv.resize(frame, (640, 480))
    #Ens tornara de color gris les cares
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY )

    faces=face_cascade.detectMultiScale(gray, 1.1,4)

    for(x,y,w,h) in faces:
        cv.rectangle(frame, (x, y), (x+w, y+h), (0,0,255), 2)

        cv.imshow('nanoCam',frame)
        cv.moveWindow('nanoCam', 0,0)
        if cv.waitKey(1)==ord('q'):
            break

    cam.release()
    cv.destroyAllWindows()