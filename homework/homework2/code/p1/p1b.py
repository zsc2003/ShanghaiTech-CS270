import numpy as np
import matplotlib.pyplot as plt

def Gaussian_high_pass_filter(size, D0):
    filter = np.zeros((size, size))
    for i in range(size):
        for j in range(size):
            filter[i, j] = 1 - np.exp(-((i - size // 2) ** 2 + (j - size // 2) ** 2) / (2 * D0 ** 2))
    return filter

origin_image = plt.imread('images/origin_images/Figure1.tif')



