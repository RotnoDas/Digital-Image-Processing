import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('lab_1_image.jpg', 0)

if image is None:
    print("Couldn't read image")
else:
    threshold_value = 127
    binary_image = np.zeros_like(image)
    binary_image[image >= threshold_value] = 255
    _, binary_cv2 = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY)

    plt.figure(figsize=(15, 5))
    plt.subplot(1, 3, 1)
    plt.imshow(image, cmap='gray', vmin=0, vmax=255)
    plt.title('Original image')
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.imshow(binary_image, cmap='gray', vmin=0, vmax=255)
    plt.title('Binary image')
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.imshow(binary_cv2, cmap='gray', vmin=0, vmax=255)
    plt.title('Binary image')
    plt.axis('off')

    plt.tight_layout()
    plt.show()