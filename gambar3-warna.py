# memisah gambar menjadi 3 warna dasar, dan disimpan pada variabel masing2 b,g,r
b, g, r = cv2.split(img)
b = img[...,0] #blue channel
g = img[...,1]
r = img[...,2]

cv2_imshow(r);