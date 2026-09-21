#Morphological boundary extraction using erosion
import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('lab_1_image.jpg', 0)

if image is None:
    print("Couldn't read image")
else:
    _, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
    kernel = np.ones((3, 3), np.uint8)
    eroded_image = cv2.erode(binary_image, kernel, iterations=1)
    boundary_image = cv2.subtract(binary_image, eroded_image)

    plt.figure(figsize=(15, 5))
    plt.subplot(1, 3, 1)
    plt.imshow(binary_image, cmap='gray', vmin=0, vmax=255)
    plt.title('Original Binary Image')
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.imshow(eroded_image, cmap='gray', vmin=0, vmax=255)
    plt.title('Eroded Image')
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.imshow(boundary_image, cmap='gray', vmin=0, vmax=255)
    plt.title('Boundary Image')
    plt.axis('off')

    plt.tight_layout()
    plt.show()