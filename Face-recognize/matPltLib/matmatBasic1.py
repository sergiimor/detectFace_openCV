import matplotlib.pyplot as plt
import cv2 as cv

print(cv.__version__)



cam=cv.VideoCapture(0)

while True:
    ret, frame=cam.read()
    #tinc una finestra que es diu picam i vaig ficant els frames que trec de cam.read()
    cv.imshow('piCam', frame)

    #mirem si la tecla que cliquem es la q i si es entre a la q sutilitze per surtir del programa
    if cv.waitKey(1)==ord('q'):
        break

cam.release()
cv.destroyAllWindows()