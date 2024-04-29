import numpy as np
import matplotlib.pyplot as plt

origin_image = plt.imread('images/origin_images/blurred.tif')

w, h = origin_image.shape
P = 2 ** np.ceil(np.log2(w)).astype(int)
Q = 2 ** np.ceil(np.log2(h)).astype(int)


