import cv2
import mediapipe as mp
import time

class FaceMeshDetector():
    
    def __init__(self, mode=False, maxNum=1, detectionCon=0.5, trackingCon=0.5):
        
        self.mode = mode
        self.maxNum = maxNum
        self.detectionCon = detectionCon
        self.trackingCon = trackingCon
        
        self.mpDraw = mp.solutions.drawing_utils
        self.mpFaceMesh = mp.solutions.face_mesh
        self.faceMesh = self.mpFaceMesh.FaceMesh(
            static_image_mode = self.mode,
            max_num_faces = self.maxNum,
            min_detection_confidence = self.detectionCon,
            min_tracking_confidence = self.trackingCon
        )
        self.drawSpec = self.mpDraw.DrawingSpec(thickness=1, circle_radius=1)

    def findFaceMesh(self, img, draw=True):
    
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.faceMesh.process(imgRGB)
        faces = []
        
        if self.results.multi_face_landmarks:
            for facelms in self.results.multi_face_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, facelms, mp.solutions.face_mesh_connections.FACEMESH_TESSELATION, self.drawSpec, self.drawSpec)
                
                lmList = []
                for id, lm in enumerate(facelms.landmark):
                    ih, iw, ic = img.shape
                    x, y = int(lm.x*iw), int(lm.y*ih)
                    # cv2.putText(img, str(id), (x, y),  cv2.FONT_HERSHEY_PLAIN, 0.7, (0, 0, 255), 1)

                    lmList.append([id, x, y])
                    
                faces.append(lmList)
                    
        return img, faces
    

def main():
    cam = cv2.VideoCapture(0)
    pTime = 0
        
    while True:
        success, img = cam.read()
        detector = FaceMeshDetector()
        img, faces = detector.findFaceMesh(img)
        if len(faces):
            print(len(faces[0]))
        
        cTime = time.time()
        fps = 1/(cTime - pTime)
        pTime = cTime
        
        cv2.putText(img, f'FPS: {int(fps)}', (10, 70),  cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 255), 2)
        cv2.imshow("Image", img)
        cv2.waitKey(1)

if __name__ == "__main__":
    main()