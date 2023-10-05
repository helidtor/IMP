import cv2
import numpy as np
import matplotlib.pyplot as plt

def create_bandpass_kernel(low_cutoff, high_cutoff, kernel_size):
    kernel = np.ones((kernel_size, kernel_size), np.float32) / (kernel_size ** 2)
    bandpass_low = cv2.getGaussianKernel(low_cutoff, -1)
    bandpass_high = cv2.getGaussianKernel(high_cutoff, -1)
    bandpass_low = cv2.resize(bandpass_low, (kernel_size, 1))
    bandpass_high = cv2.resize(bandpass_high, (kernel_size, 1))
    bandpass = bandpass_high - bandpass_low
    bandpass = bandpass.reshape(-1, 1)
    kernel = kernel * bandpass
    return kernel

def apply_bandpass_filter(image, low_cutoff, high_cutoff, kernel_size):
    bandpass_kernel = create_bandpass_kernel(low_cutoff, high_cutoff, kernel_size)
    bandpass_img = cv2.filter2D(image, -1, bandpass_kernel)
    return bandpass_img

# Read image from file
img = cv2.imread('D:/fall2023/IMP301/xulyanh/image.jpg', cv2.IMREAD_GRAYSCALE)

# Check image shape
print("Image Shape:", img.shape)

# Set parameters for bandpass filter
low_cutoff = 10
high_cutoff = 50
kernel_size = 15

# Apply bandpass filter
result_img = apply_bandpass_filter(img, low_cutoff, high_cutoff, kernel_size)

# Visualize images
plt.subplot(1, 2, 1), plt.imshow(img, cmap='gray'), plt.title('Original Image')
plt.subplot(1, 2, 2), plt.imshow(result_img, cmap='gray'), plt.title('Filtered Image')
plt.show()
