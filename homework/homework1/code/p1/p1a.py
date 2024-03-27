import matplotlib.pyplot as plt
from p1_count_gray_num import count_gray_num

origin_grain = plt.imread('./origin_images/grain.tif')
gray_num = count_gray_num(origin_grain)

plt.bar(range(256), gray_num)
plt.xlabel('gray level')
plt.ylabel('number of pixels')
plt.title('histogram of grain.tif')
plt.show()