import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('lab_1_image.jpg', 0)
if image is None:
    print("Couldn't read image")
else:
    r = np.array(image, dtype=float)
    r_min = np.min(image)
    r_max = np.max(image)
    stretched_image = ((r - r_min) / (r_max - r_min)) * 255
    stretched_image = np.array(stretched_image, dtype=np.uint8)

    lower_bound = 100
    upper_bound = 180
    background = np.zeros_like(image)
    mask = (image >= lower_bound) & (image <= upper_bound)
    background[mask] = 255

    plt.figure(figsize=(10, 8))
    
    plt.subplot(2, 2, 1)
    plt.imshow(image, cmap='gray', vmin=0, vmax=255)
    plt.title('Original Image')
    plt.axis('off')

    plt.subplot(2, 2, 2)
    plt.imshow(stretched_image, cmap='gray', vmin=0, vmax=255)
    plt.title('Stretched Image')
    plt.axis('off')

    plt.subplot(2, 2, 3)
    plt.imshow(background, cmap='gray', vmin=0, vmax=255)
    plt.title('Gray Level Sliced')
    plt.axis('off')

    plt.tight_layout()
    plt.show()