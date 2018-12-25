# import numpy as np
import cv2

cap = cv2.VideoCapture(0)
a = 0;
while True:
    a = a + 1
    check, frame = cap.read()

    print(check)

    cv2.imshow('atul', frame)
    key = cv2.waitKey(1)
    if (key == ord('q')):
        break
print(a)  # print the number of frames
cap.release()
cv2.destroyAllWindows()