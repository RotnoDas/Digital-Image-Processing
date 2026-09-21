import cv2
import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# STEP 1: Load the Image
# ==========================================
image = cv2.imread('lab_1_image.jpg', 0)

if image is None:
    print("Couldn't read image")
else:
    height = image.shape[0]
    width = image.shape[1]
    total_pixels = height * width

    # ==========================================
    # STEP 2: Calculate Custom Histogram 
    # ==========================================
    histogram = [0] * 256
    for row in range(height):
        for col in range(width):
            pixel = image[row, col]
            histogram[pixel] += 1

    # ==========================================
    # STEP 3: Calculate PDF and CDF
    # ==========================================
    pdf = [0.0] * 256
    cdf = [0.0] * 256
    
    cumulative_sum = 0.0
    for i in range(256):
        # PDF: Number of this pixel / Total pixels
        pdf[i] = histogram[i] / total_pixels
        
        # CDF: Add current PDF to the running total
        cumulative_sum += pdf[i]
        cdf[i] = cumulative_sum

    # ==========================================
    # STEP 4: Create Transformation Map
    # ==========================================
    mapping = [0] * 256
    for i in range(256):
        # Formula: round(CDF * 255)
        mapping[i] = round(cdf[i] * 255)

    # ==========================================
    # STEP 5: Create the New Equalized Image
    # ==========================================
    # Make a blank canvas of the exact same size
    equalized_image = np.zeros((height, width), dtype=np.uint8)
    equalized_histogram = [0] * 256
    
    # Look at every old pixel, and replace it with the new mapped value
    for row in range(height):
        for col in range(width):
            old_pixel = image[row, col]
            new_pixel = mapping[old_pixel]
            equalized_image[row, col] = new_pixel
            equalized_histogram[new_pixel] += 1

    # ==========================================
    # STEP 6: Plotting (Your exact plotting code)
    # ==========================================
    plt.figure(figsize=(12, 8))
    
    plt.subplot(2, 2, 1)
    plt.imshow(image, cmap='gray', vmin=0, vmax=255)
    plt.title('Original Image')
    plt.axis('off')

    plt.subplot(2, 2, 2)
    plt.imshow(equalized_image, cmap='gray', vmin=0, vmax=255)
    plt.title('Equalized Image (From Scratch)')
    plt.axis('off')

    plt.subplot(2, 2, 3)
    x_axis_values = list(range(256))
    plt.bar(x_axis_values, histogram, color='gray', width=1)
    plt.title('Original Histogram')
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Pixel Count')

    plt.subplot(2, 2, 4)
    plt.bar(x_axis_values, equalized_histogram, color='black', width=1)
    plt.title('Equalized Histogram (From Scratch)')
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Pixel Count')

    plt.tight_layout()
    plt.show()