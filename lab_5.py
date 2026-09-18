import cv2
import numpy as np
import matplotlib.pyplot as plt

image_a = np.zeros((300, 300), dtype=np.uint8)
image_a[50:250, 50:150] = 255

image_b = np.zeros((300, 300), dtype=np.uint8)
cv2.circle(image_b, (150, 150), 75, 255, -1)

added_image = cv2.add(image_a, image_b)
subtracted_image = cv2.subtract(image_a, image_b)
multiplied_image = cv2.multiply(image_a, image_b)
divided_image = cv2.divide(image_a, image_b)

and_image = cv2.bitwise_and(image_a, image_b)
or_image = cv2.bitwise_or(image_a, image_b)
xor_image = cv2.bitwise_xor(image_a, image_b)
not_image = cv2.bitwise_not(image_a)

plt.figure(figsize=(16, 8))
plt.subplot(2, 5, 1)
plt.imshow(image_a, cmap='gray', vmin=0, vmax=255)
plt.title('original image a')
plt.axis('off')

plt.subplot(2, 5, 2)
plt.imshow(image_b, cmap='gray', vmin=0, vmax=255)
plt.title('original image b')
plt.axis('off')

plt.subplot(2, 5, 3)
plt.imshow(added_image, cmap='gray', vmin=0, vmax=255)
plt.title('added image')
plt.axis('off')

plt.subplot(2, 5, 4)
plt.imshow(subtracted_image, cmap='gray', vmin=0, vmax=255)
plt.title('subtracted image')
plt.axis('off')

plt.subplot(2, 5, 5)
plt.imshow(multiplied_image, cmap='gray', vmin=0, vmax=255)
plt.title('multiplied image')
plt.axis('off')

plt.subplot(2, 5, 6)
plt.imshow(divided_image, cmap='gray', vmin=0, vmax=255)
plt.title('divided image')
plt.axis('off')

plt.subplot(2, 5, 7)
plt.imshow(and_image, cmap='gray', vmin=0, vmax=255)
plt.title('and image')
plt.axis('off')

plt.subplot(2, 5, 8)
plt.imshow(or_image, cmap='gray', vmin=0, vmax=255)
plt.title('or image')
plt.axis('off')

plt.subplot(2, 5, 9)
plt.imshow(xor_image, cmap='gray', vmin=0, vmax=255)
plt.title('xor image')
plt.axis('off')

plt.subplot(2, 5, 10)
plt.imshow(not_image, cmap='gray', vmin=0, vmax=255)
plt.title('not image')
plt.axis('off')

plt.tight_layout()    
plt.show()