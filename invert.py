import cv2

# Đọc ảnh gốc
image = cv2.imread('D:/fall2023/IMP301/xulyanh/img5.jpg')
cv2.imshow('Image', image)

# Chuyển đổi trắng thành đen và ngược lại
inverted_image = cv2.bitwise_not(image)

# Lưu ảnh kết quả vào tệp mới
cv2.imwrite('inverted_image.jpg', inverted_image)

# Hiển thị ảnh kết quả (tùy chọn)
cv2.imshow('Inverted Image', inverted_image)
cv2.waitKey(0)
cv2.destroyAllWindows()