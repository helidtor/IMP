def find_nearest_above(my_array, target):
    diff = my_array - target
    mask = np.ma.less_equal(diff, -1)
    # We need to mask the negative differences
    # since we are looking for values above
    if np.all(mask):
        c = np.abs(diff).argmin()
        return c  # returns min index of the nearest if target is greater than any value
    masked_diff = np.ma.masked_array(diff, mask)
    return masked_diff.argmin()


def hist_match(original, specified):
    oldshape = original.shape
    original = original.ravel()
    specified = specified.ravel()

    # lấy r và n của hình original và hình specified
    original_img_values, bin_idx, s_counts = np.unique(original, return_inverse=True, return_counts=True)
    specified_img_values, t_counts = np.unique(specified, return_counts=True)

    # Tính s_k cho ảnh gốc
    s_original = np.cumsum(s_counts).astype(np.float64)
    s_original /= s_original[-1]

    # Tính s_k cho ảnh specified
    s_spec = np.cumsum(t_counts).astype(np.float64)
    s_spec /= s_spec[-1]

    # Làm tròn giá trị
    ori_round = np.around(s_original * 255)
    spec_round = np.around(s_spec * 255)

    # Mapping giá trị đã làm tròn
    b = []
    for data in ori_round[:]:
        b.append(find_nearest_above(spec_round, data))
    b = np.array(b, dtype='uint8')

    return b[bin_idx].reshape(oldshape)


import cv2
import numpy as np
import matplotlib.pyplot as plt

# chọn ảnh
original = cv2.imread('image1.jpg')
specified = cv2.imread('spec.jpg')

# thực hiện Histogram Matching
a = hist_match(original, specified)
result = np.array(a, dtype='uint8')

# Tính toán histogram của hình ảnh gốc và hình ảnh đã cân bằng
hist_original = cv2.calcHist([original], [0], None, [256], [0, 256])
hist_equalized = cv2.calcHist([result], [0], None, [256], [0, 256])
hist_specified = cv2.calcHist([specified], [0], None, [256], [0, 256])

# Vẽ biểu đồ histogram
plt.figure(figsize=(10, 5))

# Biểu đồ histogram của hình ảnh gốc (màu đen)
plt.plot(hist_original, color='black', label='Original Histogram')

# Biểu đồ histogram của hình ảnh đã cân bằng (màu đỏ)
plt.plot(hist_equalized, color='red', label='Matching Histogram')

# Biểu đồ histogram của hình ảnh đã cân bằng (màu xanh)
plt.plot(hist_specified, color='blue', label='Specified Histogram')

# Đặt tiêu đề và nhãn cho biểu đồ
plt.title('Compare Histogram')

# Display the image
cv2.imshow('result', result)
cv2.imshow('original', original)
cv2.imshow('specified', specified)
plt.legend()
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()