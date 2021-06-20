import cv2
import numpy as np
from PIL import Image


cap = cv2.VideoCapture(0)

while cap.isOpened():

    ret, back = cap.read()

    if ret:

        cv2.imshow("Image", back)

        if cv2.waitKey(5) == ord("q"):
            cv2.imwrite('img.jpg', back)
            break

cap.release()
cv2.destroyAllWindows()
