import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("lab_1_image.jpg", 0)
binary_img = np.where(img >= 127, 255, 0).astype(np.uint8)


kernel = np.ones((5, 5), dtype=np.uint8)


erosion = cv2.erode(binary_img, kernel, iterations=1)
dilation = cv2.dilate(binary_img, kernel, iterations=1)
opening = cv2.morphologyEx(binary_img, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(binary_img, cv2.MORPH_CLOSE, kernel)


plt.figure(figsize=(12, 8))

plt.subplot(2, 3, 1)
plt.imshow(binary_img, cmap="gray")
plt.title("Binary Input Image")
plt.axis("off")

plt.subplot(2, 3, 2)
plt.imshow(erosion, cmap="gray")
plt.title("Erosion")
plt.axis("off")

plt.subplot(2, 3, 3)
plt.imshow(dilation, cmap="gray")
plt.title("Dilation")
plt.axis("off")

plt.subplot(2, 3, 4)
plt.imshow(opening, cmap="gray")
plt.title("Opening")
plt.axis("off")

plt.subplot(2, 3, 5)
plt.imshow(closing, cmap="gray")
plt.title("Closing")
plt.axis("off")

plt.tight_layout()
plt.show()