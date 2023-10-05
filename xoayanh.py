import cv2
import numpy as np

# Đọc ảnh gốc
image = cv2.imread('D:/fall2023/IMP301/xulyanh/img5.jpg')
cv2.imshow(' Image', image)
# Đặt góc xoay (đơn vị là độ)
alpha = -45  # Ví dụ: xoay 30 độ

# Tính toán ma trận biến đổi xoay
height, width = image.shape[:2]
center = (width // 2, height // 2)
rotation_matrix = cv2.getRotationMatrix2D(center, alpha, 1.0)

# Thực hiện xoay ảnh
rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))

# Lưu ảnh sau khi xoay vào một tệp mới
cv2.imwrite('rotated_image.jpg', rotated_image)

# Hiển thị ảnh sau khi xoay (tùy chọn)
cv2.imshow('Rotated Image', rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()