import matplotlib.pyplot as plt
from p1_count_gray_num import count_gray_num

origin_grain = plt.imread('./origin_images/grain.tif')
gray_num = count_gray_num(origin_grain)


fig, ax = plt.subplots(1, 2)
        
# show the origin image
ax[0].imshow(origin_grain, cmap='gray')
ax[0].set_title('origin image')

# show the histogram of grain.tif
ax[1].bar(range(256), gray_num)
ax[1].set_xlabel('gray level')
ax[1].set_ylabel('number of pixels')
ax[1].set_title('histogram of grain.tif')
plt.show()