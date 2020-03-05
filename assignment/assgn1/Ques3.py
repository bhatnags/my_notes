import cv2

cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def detect(img, cascade):
    rects = cascade.detectMultiScale(img, scaleFactor=1.3, 
                                     minNeighbors=4, minSize=(30, 30),
                                     flags = cv2.CASCADE_SCALE_IMAGE)
    if len(rects) == 0:
        return []
    rects[:,2:] += rects[:,:2]
    return rects

def draw_rects(img, rects, color):
    for x1, y1, x2, y2 in rects:
        cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)

def find_and_blur(bw, frame): 
    # detect all faces
    # faces = detect(bw, cascade)
    faces = cascade.detectMultiScale(bw)#, scaleFactor=1.3, minNeighbors=4, minSize=(30, 30), flags = cv2.CASCADE_SCALE_IMAGE)
    if len(faces) == 0:
        return []
    faces[:,2:] += faces[:,:2]
    #faces = cascade.detectMultiScale(bw, scaleFactor=1.3, minNeighbors=4, minSize=(30, 30), flags = cv2.cv.CV_HAAR_SCALE_IMAGE
    # get the locations of the faces
    vis = frame.copy()
    draw_rects(vis, faces, (0, 255, 0))
    for x1, y1, x2, y2 in faces:
        roi = bw[y1:y2, x1:x2]
        vis_roi = vis[y1:y2, x1:x2]
        subrects = detect(roi.copy())#, nested)
        draw_rects(vis_roi, subrects, (255, 0, 0))
        # blur the colored image
        blur = cv2.GaussianBlur(vis_roi, (101,101), 0)        
        # Insert ROI back into image
        vis[y1:y2, x1:x2] = blur            
    return vis


import os
from os import path
f_loc = 'F:\\aindra\\video.mp4'

if os.path.isfile(f_loc):
    cap = cv2.VideoCapture(f_loc)
    
    while(cap.isOpened()):
        # Read frame-by-frame
        ret, frame = cap.read()
    
        # transform color -> grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
        # detect the face and blur it
        blur = find_and_blur(gray, frame)

        # draw_str(vis, (20, 20))#, 'time: %.1f ms' % (dt*1000))
        #cv2.imshow('facedetect', vis)
        #if 0xFF & cv2.waitKey(5) == 27:

        # Display the resulting frame
        cv2.imshow('frame',gray)
        # break if q is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # turn video off        
    # cap.release()
    # close video  window
    cv2.destroyAllWindows()




