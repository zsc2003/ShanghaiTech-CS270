import matplotlib.pyplot as plt
from p1_count_gray_num import count_gray_num
import numpy as np

origin_grain = plt.imread('./origin_images/grain.tif')
gray_num = count_gray_num(origin_grain)
w, h = origin_grain.shape

prefix_sum = np.cumsum(gray_num) / (w * h)
prefix_gray = np.round(prefix_sum * 255).astype(np.uint8)

# histogram of grain.tif after applying histogram equalization
equalized_grain = np.zeros_like(origin_grain, dtype=np.uint8)
for i in range(w):
    for j in range(h):
        equalized_grain[i][j] = prefix_gray[int(origin_grain[i][j])]

# show the equalized image
plt.imshow(equalized_grain, cmap='gray')
plt.title('histogram equalized image')
plt.show()

# show the histogram of grain.tif after applying histogram equalization
plt.bar(range(256), count_gray_num(equalized_grain))
plt.xlabel('gray level')
plt.ylabel('number of pixels')
plt.title('histogram of histogram equalized image')
plt.show()