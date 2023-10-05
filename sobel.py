import cv2
import numpy as np

# Đọc hình ảnh
image = cv2.imread('image1.jpg', cv2.IMREAD_GRAYSCALE)

# Kiểm tra xem hình ảnh đã được đọc thành công chưa
if image is None:
    print("Không thể đọc hình ảnh. Đảm bảo đường dẫn đến tệp đúng.")
else:
    # Áp dụng bộ lọc Sobel để tính đạo hàm theo x và ya 
    sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)

    #Hiển thị Sobel X và Y
    sobel_x = cv2.convertScaleAbs(sobel_x)
    cv2.imshow('X', sobel_x)
    sobel_y = cv2.convertScaleAbs(sobel_y)
    cv2.imshow('Y', sobel_y)

    # Tổng hợp hai đạo hàm để tính gradient tổng quát
    gradient = cv2.addWeighted(sobel_x, 0.5, sobel_y, 0.5, 0)
    gradient = cv2.convertScaleAbs(gradient)

    # Hiển thị hình ảnh gốc và gradient X+Y
    cv2.imshow('original image', image)
    cv2.imshow('X+Y', gradient)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
