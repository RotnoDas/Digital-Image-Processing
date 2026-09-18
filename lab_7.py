import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('lab_1_image.jpg', 0)

if image is None:
    print("Couldn't read image")
else:
    kernel_smooth = np.ones((3, 3), np.float32) / 9.0
    kernel_sharpen = np.array([
        [0, -1, 0],
        [-1, 5, -1],
        [0, -1, 0]
    ], dtype=np.float32)
    kernel_edge = np.array([
        [-1, -1, -1],
        [-1, 8, -1],
        [-1, -1, -1]
    ], dtype=np.float32)

    smoothed_image = cv2.filter2D(image, -1, kernel_smooth)
    sharpened_image = cv2.filter2D(image, -1, kernel_sharpen)
    edge_image = cv2.filter2D(image, -1, kernel_edge)

    plt.figure(figsize=(12, 10))
    plt.subplot(2, 2, 1)
    plt.imshow(image, cmap='gray', vmin=0, vmax=255)
    plt.title('Original image')
    plt.axis('off')

    plt.subplot(2, 2, 2)
    plt.imshow(smoothed_image, cmap='gray', vmin=0, vmax=255)
    plt.title('Smoothed image')
    plt.axis('off')

    plt.subplot(2, 2, 3)
    plt.imshow(sharpened_image, cmap='gray', vmin=0, vmax=255)
    plt.title('Sharpened image')
    plt.axis('off')

    plt.subplot(2, 2, 4)
    plt.imshow(edge_image, cmap='gray', vmin=0, vmax=255)
    plt.title('Edge detected')
    plt.axis('off')

    plt.tight_layout()
    plt.show()
