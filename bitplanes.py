import cv2
import numpy as np

# Đọc ảnh
image = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

# Lấy số lượng bit planes bạn muốn trích xuất (ví dụ: 4 bit planes)
num_planes = 7


# Tạo các bit planes
bit_planes = [np.bitwise_and(image, 2**i) for i in range(num_planes)]

# Hiển thị các bit planes
for i, plane in enumerate(bit_planes):
    cv2.imshow(f'Bit Plane {i}', plane * 255)  # Để hiển thị đúng, bạn có thể nhân với 255
    cv2.waitKey(0)
    cv2.destroyAllWindows()
