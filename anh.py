import cv2
import numpy as np

# Đọc ảnh gốc
image = cv2.imread('D:/fall2023/IMP301/xulyanh/image.jpg')
image2 = cv2.imread('D:/fall2023/IMP301/xulyanh/anh2.webp')


new_width = 900
new_height = 500
new_size = (new_width, new_height)

# Thay đổi kích thước ảnh
resized_image = cv2.resize(image2, new_size)

cv2.imwrite('resized_image.jpg', resized_image)

# Hiển thị ảnh mới (tùy chọn)
cv2.imshow('Resized Image', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Tăng độ tương phản bằng cách sử dụng phép nhân




contrast_increase = 0.4 # Giá trị này thể hiện mức độ tăng độ tương phản
contrasted_image = np.clip(image * contrast_increase, 0, 255).astype(np.uint8)
contrasted_image2 = np.clip(resized_image * contrast_increase, 0, 255).astype(np.uint8)




# Trừ giá trị pixel ban đầu từ ảnh đã tăng độ tương phản
difference_image = contrasted_image - image
difference_image2 = contrasted_image2 - contrasted_image

cv2.imshow('contrasted_image', contrasted_image)
cv2.imshow('contrasted_image', resized_image)

# Lưu ảnh kết quả vào tệp mới
cv2.imwrite('difference_image.jpg', difference_image)
cv2.imwrite('difference_image.jpg', difference_image2)

# Hiển thị ảnh kết quả (tùy chọn)
cv2.imshow('Difference Image', difference_image)
cv2.imshow('Difference Image', difference_image2)
cv2.waitKey(0)
cv2.destroyAllWindows()