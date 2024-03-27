import matplotlib.pyplot as plt
import numpy as np
from p2_normalization import normalization
from p2_convolution import convolution

origin_lena = plt.imread('./origin_images/moon.jpg')
w, h = origin_lena.shape

# Laplacian_kernel
Laplacian_kernel = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
Laplacian_image = convolution(origin_lena, Laplacian_kernel)
Laplacian_image = normalization(Laplacian_image)
plt.imshow(Laplacian_image, cmap='gray')
plt.title('Laplacian kernel')
plt.show()