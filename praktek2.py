import cv2
import numpy as np

# membaca file citra pada komputer
citra = cv2.imread("D:/citra/rgb.jpeg")

b = citra[:, :, 0]
g = citra[:, :, 1]
r = citra[:, :, 2]
# b,g,r=cv2.split(citra)

# menyimpan jumlah baris dan kolom
jum_baris = len(citra)
jum_kolom = len(citra[0])

# menyiapkan citra baru dengan nilai nol
citra_grayscale = np.zeros((jum_baris, jum_kolom))

for i in range(jum_baris):
    for j in range(jum_kolom):
        citra_grayscale[i, j] = round(
            0.299 * r[i, j] + 0.587 * g[i, j] + 0.114 * b[i, j])


# convert ke int yang bernilai positif
citra_grayscale = citra_grayscale.astype(np.uint8)

# menampilkan citra digital yang sudah dibaca
cv2.imshow("gray", citra_grayscale)

# menampilkan matriks pada citra
print(citra_grayscale)


# menuggu sampai user menekan sembarang tombol
cv2.waitKey()
