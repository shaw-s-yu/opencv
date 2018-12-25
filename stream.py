import numpy as np
import cv2
import time

cap = cv2.VideoCapture(0)
time.sleep(1)   #warm up camera

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    frame=cv2.flip(frame,1)
    # Our operations on the frame come her

    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) == 27:
        break
    if cv2.waitKey(1)== ord('s'):
        cv2.imwrite('jjj.png', frame)
        break

# When everything done, release the capture
time.sleep(1000)
cap.release()
cv2.destroyAllWindows()
