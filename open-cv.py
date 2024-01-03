import cv2

from google.colab.patches import cv2_imshow

img= cv2.imread("th (2).jpeg")
gray_image = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
cv2_imshow(gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("gambar-bgr.jpeg", gray_image)