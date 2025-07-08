import cv2
import faceMeshModule as fmm
import time
import numpy as np
import serial

cap = cv2.VideoCapture(0)
pTime = 0
angle = 90

detector = fmm.FaceMeshDetector(detectionCon=0.75)

arduinoData = serial.Serial('COM3', 9600)
time.sleep(2)  # Wait for the connection to establish

while True:
    success, img = cap.read()
    if not success: break
    img = cv2.flip(img, 1)
    img = cv2.resize(img, (1366, 780))
    img, faces = detector.findFaceMesh(img)
    
    if len(faces):
        myface = faces[0]
        nosetip = myface[4]
        cv2.circle(img, (nosetip[1], nosetip[2]), 5, (0, 0, 255), cv2.FILLED)
        
        if (myface[127][1] >= 400 and myface[457][1] <= 940 and myface[10][2] >= 80 and myface[152][2] <= 650): 
            cv2.putText(img, "Move your face within the box", (400, 70), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 255, 0), 2)
            cv2.rectangle(img, (400, 650), (940, 80), (0, 255, 0), 2)
            
            angle = int(np.interp(nosetip[1], [400, 940], [180, 0]))
        else:
            cv2.putText(img, "Place your face in the box", (400, 70), cv2.FONT_HERSHEY_DUPLEX, 1.1, (0, 0, 255), 2)
            cv2.rectangle(img, (400, 650), (940, 80), (0, 0, 255), 2)
            
            angle = 90
        
        arduinoData.write((str(int(angle)) + '\r').encode('utf-8'))
        
    print(angle if faces else "No face detected")
    
    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (10, 30), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 255, 255), 2)
    
    cv2.imshow("Servo Controller with Face Movement", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break