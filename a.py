import cv2
from qrcheck import qrck

img = cv2.imread("./qr.jpg")
a = qrck(img)
print(a)