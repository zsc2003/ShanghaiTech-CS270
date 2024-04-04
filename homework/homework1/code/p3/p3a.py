import matplotlib.pyplot as plt
import numpy as np

origin_lena = plt.imread('./origin_images/lena_noisy.tif')
w, h = origin_lena.shape

fig, ax = plt.subplots(2, 2)
ax[0, 0].imshow(origin_lena, cmap='gray')
ax[0, 0].set_title('origin lena')

# median filter
for kernel_range in range(1, 4):
    kernel_size = 2 * kernel_range + 1
    median_lena = np.zeros((w, h), dtype=np.uint8)

    for i in range(w):
        for j in range(h):

            neighbouring_pixels = []
            for x in range(-kernel_range, kernel_range + 1):
                for y in range(-kernel_range, kernel_range + 1):
                    if i + x >= 0 and i + x < w and j + y >= 0 and j + y < h:
                        neighbouring_pixels.append(origin_lena[i + x, j + y])
            
            median_lena[i, j] = np.uint8(np.median(neighbouring_pixels))

    row = kernel_range // 2
    col = kernel_range % 2
    ax[row, col].imshow(median_lena, cmap='gray')
    ax[row, col].set_title('median filtered lena with kernel size ' + str(kernel_size))

plt.show()