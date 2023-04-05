import cv2
import numpy as np

#membaca file citra pada komputer
citra =cv2.imread("D:/citra/rgb.jpeg")




citra_gray=cv2.cvtColor(citra,cv2.COLOR_BGR2GRAY)
#menampilkan citra digital yang sudah dibaca
cv2.imshow("celsea-blue",citra)
cv2.imshow("celsea-green",citra_gray)

print(citra_gray)



#menuggu sampai user menekan sembarang tombol
cv2.waitKey()