import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('lab_1_image.jpg', 0)

if image is None:
    print("Couldn't read image")
else:
    negative_image = 255 - image

    image_float = np.array(image, dtype=float)
    c_log = 255 / np.log(1 + np.max(image_float))
    log_transformed_image = c_log * np.log(1 + image_float)
    log_image = np.array(log_transformed_image, dtype=np.uint8)

    gamma = 2.5
    image_normalized = image / 255.0
    gamma_image = np.power(image_normalized, gamma)
    gamma_image = gamma_image * 255.0
    gamma_image = np.array(gamma_image, dtype=np.uint8)

plt.figure(figsize=(10, 8))

plt.subplot(2, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.imshow(negative_image, cmap='gray')
plt.title('Negative Image')
plt.axis('off')

plt.subplot(2, 2, 3)
plt.imshow(log_image, cmap='gray')
plt.title('Log Transformed image')
plt.axis('off')

plt.subplot(2, 2, 4)
plt.imshow(gamma_image, cmap='gray')
plt.title('Gamma Transformed image')
plt.axis('off')

plt.tight_layout()

plt.show()