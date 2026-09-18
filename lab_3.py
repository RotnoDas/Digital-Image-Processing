import cv2
import matplotlib.pyplot as plt

image = cv2.imread('lab_1_image.jpg', 0)

if image is None:
    print("Couldn't read image")
else:
    histogram = [0] * 256
    height = image.shape[0]
    width = image.shape[1]
    for row in range(height):
        for col in range(width):
            pixel = image[row, col]
            histogram[pixel] += 1

    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(image, cmap='gray', vmin=0, vmax=255)
    plt.title('Original Image')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    x_axis_values = list(range(256))
    plt.bar(x_axis_values, histogram, color='gray', width=1)
    plt.title('Histogram')
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Pixel Count')

    plt.tight_layout()
    plt.show()