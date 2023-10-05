import cv2
import numpy as np

# Đọc hình ảnh
img = cv2.imread('image.jpg') 

# Tạo các bộ lọc
# Tạo các bộ lọc 
lowpass = np.ones((5,5),np.float32)/25

# Sửa kích thước bộ lọc highpass thành 5x5 
highpass = np.array([[-1,-1,-1,-1,-1],  
                    [-1,-1,-1,-1,-1],
                    [-1,-1,9,-1,-1],
                    [-1,-1,-1,-1,-1],
                    [-1,-1,-1,-1,-1]])

bandreject = np.ones((5,5),np.float32)/25
bandreject[2,2] = 0

bandpass = highpass - lowpass

# Áp dụng các bộ lọc 
low_img = cv2.filter2D(img, -1, lowpass)
high_img = cv2.filter2D(img, -1, highpass) 
bandreject_img = cv2.filter2D(img, -1, bandreject)
bandpass_img = cv2.filter2D(img, -1, bandpass)

# Hiển thị kết quả
cv2.imshow('Original', img)
cv2.imshow('Low pass', low_img) 
cv2.imshow('High pass', high_img)
cv2.imshow('Band reject', bandreject_img) 
cv2.imshow('Band pass', bandpass_img)
cv2.waitKey()
cv2.destroyAllWindows()