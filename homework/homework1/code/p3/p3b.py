import matplotlib.pyplot as plt
import numpy as np
from p3_convolution import convolution

origin_lena = plt.imread('./origin_images/lena_noisy.tif')
w, h = origin_lena.shape
sigma = 1

# Gaussian filter
for kernel_range in range(1, 4):
    kernel_size = 2 * kernel_range + 1

    kernel = np.zeros((kernel_size, kernel_size))
    for i in range(-kernel_range, kernel_range + 1):
        for j in range(-kernel_range, kernel_range + 1):
            kernel[i + kernel_range][j + kernel_range] = np.exp(- (i ** 2 + j ** 2) / sigma ** 2 / 2)
    kernel /= np.sum(kernel)

    Gaussian_lena = convolution(origin_lena, kernel)
    Gaussian_lena = np.uint8(np.round(Gaussian_lena))
    
    plt.imshow(Gaussian_lena, cmap='gray')
    plt.title('Gaussian filtered lena with kernel size ' + str(kernel_size))
    plt.show()