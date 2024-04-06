import matplotlib.pyplot as plt
import numpy as np
from p1_count_gray_num import count_gray_num

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

fig, ax = plt.subplots(1, 2)
        
# show the equalized image
ax[0].imshow(equalized_grain, cmap='gray')
ax[0].set_title('histogram equalized image')

# show the histogram of grain.tif after applying histogram equalization
ax[1].bar(range(256), count_gray_num(equalized_grain))
ax[1].set_xlabel('gray level')
ax[1].set_ylabel('number of pixels')
ax[1].set_title('histogram of histogram equalized image')
plt.show()