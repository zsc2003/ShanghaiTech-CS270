import numpy as np
import matplotlib.pyplot as plt

from p1_convolution import convolution
from p1_normalization import normalization

origin_image = plt.imread('images/origin_images/Figure1.tif')

Sobel_x = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
Sobel_y = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])

