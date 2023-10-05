import cv2
import numpy as np

# Đọc ảnh vào
image = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

# Thực hiện log transformation
c = 1  # Hệ số giai đoạn
log_transformed = c * np.log(1 + image)

# Chuyển đổi về kiểu dữ liệu 8-bit (0-255)
log_transformed = np.uint8(log_transformed)

# Hiển thị ảnh gốc và ảnh sau khi áp dụng log transformation
cv2.imshow('Original Image', image)
cv2.imshow('Log Transformed Image', log_transformed)
cv2.waitKey(0)
cv2.destroyAllWindows()
