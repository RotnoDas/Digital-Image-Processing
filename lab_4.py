#Histogram equalisation
import cv2
import matplotlib.pyplot as plt

image = cv2.imread('lab_1_image.jpg', 0)

if image is None:
    print("Couldn't read image")
else:
    equalized_image = cv2.equalizeHist(image)

    plt.figure(figsize=(12, 8))
    plt.subplot(2, 2, 1)
    plt.imshow(image, cmap='gray', vmin=0, vmax=255)
    plt.title('Original Image')
    plt.axis('off')

    plt.subplot(2, 2, 2)
    plt.imshow(equalized_image, cmap='gray', vmin=0, vmax=255)
    plt.title('Equalized Image')
    plt.axis('off')

    plt.subplot(2, 2, 3)
    plt.hist(image.ravel(), bins=256, range=(0, 256), color='gray')
    plt.title('Histogram')
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Pixel Count')

    plt.subplot(2, 2, 4)
    plt.hist(equalized_image.ravel(), bins=256, range=(0, 256), color='black')
    plt.title('Equalized Histogram')
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Pixel Count')

    plt.tight_layout()
    plt.show()