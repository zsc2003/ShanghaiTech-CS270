import matplotlib.pyplot as plt
import numpy as np
from p2_normalization import normalization
from p2_convolution import convolution

origin_lena = plt.imread('./origin_images/moon.jpg')
w, h = origin_lena.shape

# Laplacian_kernel_sharp
Laplacian_kernel_sharp = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
Laplacian_image = convolution(origin_lena, Laplacian_kernel_sharp)

fig, ax = plt.subplots(1, 2)

ax[0].imshow(np.minimum(np.maximum(Laplacian_image, 0),255), cmap='gray')
ax[0].set_title('Laplacian kernel(drop < 0)')

ax[1].imshow(Laplacian_image, cmap='gray')
ax[1].set_title('Laplacian kernel(without dropping)')
plt.show()