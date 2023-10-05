# import cv2 
# import numpy as np

# img = cv2.imread('image1.jpg', 0) 

# out = []

# for k in range(0, 7):
#     # create an image for each k bit plane
#     plane = np.full((img.shape[0], img.shape[1]), 2 ** k, np.uint8)
#     # execute bitwise and operation
#     res = cv2.bitwise_and(plane, img)
#     # multiply ones (bit plane sliced) with 255 just for better visualization
#     x = res * 255
#     # append to the output list
#     out.append(x)

# cv2.imshow("bit plane", np.hstack(out))
# cv2.waitKey()

import cv2
import numpy as np

# Đọc ảnh đầu vào
image = cv2.imread('image1.jpg', cv2.IMREAD_GRAYSCALE)

# Kiểm tra xem ảnh đã được đọc chưa
if image is None:
    print("Không thể đọc ảnh. Hãy đảm bảo rằng đường dẫn đúng và ảnh tồn tại.")
else:
    # Tách các bit-plane
    bit_planes = [np.bitwise_and(image, 2**i) for i in range(8)]

    # Hiển thị các bit-plane
    for i, bit_plane in enumerate(bit_planes):
        cv2.imshow(f'Bit-Plane {i}', bit_plane * 255)  # Để hiển thị, nhân với 255 để chuyển về ảnh grayscale
        cv2.waitKey(0)

    # Đóng cửa sổ khi bạn nhấn phím bất kỳ
    cv2.destroyAllWindows()