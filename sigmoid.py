import cv2
import numpy as np

def sigmoid(x, a, b):
    return 1 / (1 + np.exp(-a * (x - b)))

# Đọc ảnh vào
image = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

# Thực hiện điều chỉnh độ tương phản bằng hàm sigmoid
a = 1
# Thay đổi giá trị a theo ý muốn
b = 1# Thay đổi giá trị b theo ý muốn

sigmoid_adjusted = 255 * sigmoid(image / 255.0, a, b)

# Chuyển đổi về kiểu dữ liệu 8-bit (0-255)
sigmoid_adjusted = np.uint8(sigmoid_adjusted)

# Hiển thị ảnh gốc và ảnh sau khi áp dụng hàm sigmoid
cv2.imshow('Original Image', image)
cv2.imshow('Sigmoid Adjusted Image', sigmoid_adjusted)
cv2.waitKey(0)
cv2.destroyAllWindows()
