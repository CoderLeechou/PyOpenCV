#-*-coding:UTF-8-*-
import cv2

img=cv2.imread("cat.jpg",0)
cv2.namedWindow("Image",cv2.WINDOW_NORMAL)
cv2.imshow("Image",img)
k = cv2.waitKey(0)
if k == 27: # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('catgray.png',img)
    cv2.destroyAllWindows()