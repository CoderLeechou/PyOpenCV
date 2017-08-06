# -*- coding: utf-8 -*-
import numpy as np
import cv2



cap = cv2.VideoCapture('test.mp4')
if not cap.isOpened(): cap.open()
c = 1

while (cap.isOpened()):
    ret, frame = cap.read()
    if frame is None:
        break
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', frame)
    cv2.imwrite('Image\\image' + '%s'%c + '.jpg', frame)
    c = c + 1

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()