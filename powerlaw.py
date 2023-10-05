import cv2
import numpy as np

# Đọc ảnh vào
image = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

# Thực hiện Power Law Transformation
gamma = 2.5  # Thay đổi giá trị gamma theo ý muốn
power_law = np.power(image / 255.0, gamma) * 255.0

# Chuyển đổi về kiểu dữ liệu 8-bit (0-255)
power_law = np.uint8(power_law)

# Hiển thị ảnh gốc và ảnh sau khi áp dụng Power Law Transformation
cv2.imshow('Original Image', image)
cv2.imshow('Power Law Transformed Image', power_law)
cv2.waitKey(0)
cv2.destroyAllWindows()
