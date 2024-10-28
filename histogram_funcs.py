# This file holds the algorithms to perform the histogram operations on the image.

import matplotlib.pyplot as plt
import numpy as np

#Function to plot histogram
def plot_histogram(image):
    colours = ('red', 'green', 'blue')
    for i, colour in enumerate(colours):
        histogram, bins = np.histogram(image[:, :, i], bins=256, range=(0, 256))
        plt.plot(histogram, colour)
        plt.xlim([0, 256])
    plt.title("RGB Histogram")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Frequency")
    plt.show()



# Function for aggressive histogram stretching
def aggressive_stretch(image):
    aggressive_image = np.zeros_like(image)
    for i in range(3):  # For each color channel
        min_val = np.percentile(image[:, :, i], 5)
        max_val = np.percentile(image[:, :, i], 95)
        aggressive_image[:, :, i] = np.clip((255 * (image[:, :, i] - min_val) / (max_val - min_val)), 0, 255).astype(np.uint8)
    return aggressive_image


# Function for histogram equalization
def histogram_equalization(image):
    # Convert to grayscale for equalization (apply on the V channel of HSV)
    gray = np.dot(image[..., :3], [0.299, 0.587, 0.114]).astype(np.uint8)

    # Perform histogram equalization
    hist, bins = np.histogram(gray.flatten(), 256, [0, 256])
    cdf = hist.cumsum()  # Cumulative distribution function
    cdf_normalized = cdf * 255 / cdf[-1]  # Normalize the CDF to range [0, 255]

    # Apply the CDF to the grayscale image
    img_eq = np.interp(gray.flatten(), bins[:-1], cdf_normalized).reshape(gray.shape).astype(np.uint8)

    # Convert back to RGB by scaling the V channel (HSV -> RGB)
    hsv_img = np.stack([image[..., 0], image[..., 1], img_eq], axis=-1)
    return hsv_img