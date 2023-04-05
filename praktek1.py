import cv2

#membaca file citra pada komputer
citra =cv2.imread("D:/citra/rgb.jpeg")

#menampilkan citra digital yang sudah dibaca
cv2.imshow("celsea-blue",citra[:,:,0])
cv2.imshow("celsea-green",citra[:,:,1])
cv2.imshow("celsea-red",citra[:,:,2])

# menampilkan matriks pada citra

print(citra)          # menampilkan semua chanel warna
print(citra[:,:,0])   # : yang pertama adalah baris, : yang kedua adalah kolom,)
print(citra[:,:,0])   # menampilkan semua chanel warna blue
print(citra[:,:,1])   # menampilkan semua chanel warna green
print(citra[:,:,2])   # menampilkan semua chanel warna red


#menuggu sampai user menekan sembarang tombol
cv2.waitKey()