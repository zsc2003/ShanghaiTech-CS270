import matplotlib.pyplot as plt
import numpy as np
from p2_normalization import normalization
from p2_convolution import convolution

origin_lena = plt.imread('./origin_images/moon.jpg')

# x direction
I_xx = np.array([[1], [-2], [1]])
x_direction = convolution(origin_lena, I_xx)

# y direction
I_yy = np.array([[1, -2, 1]])
y_direction = convolution(origin_lena, I_yy)

# x, y sequentially
x_y_sequential = convolution(x_direction, I_yy)

# Unseperated Laplacian kernel
Laplacian_kernel = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
unseperated = convolution(origin_lena, Laplacian_kernel)

fig, ax = plt.subplots(2, 2)

x_direction = normalization(x_direction)
ax[0, 0].imshow(x_direction, cmap='gray')
ax[0, 0].set_title('x direction kernel')

y_direction = normalization(y_direction)
ax[0, 1].imshow(y_direction, cmap='gray')
ax[0, 1].set_title('y direction kernel')

x_y_sequential = normalization(x_y_sequential)
ax[1, 0].imshow(y_direction, cmap='gray')
ax[1, 0].set_title('x, y direction sequentially')

unseperated = normalization(unseperated)
ax[1, 1].imshow(unseperated, cmap='gray')
ax[1, 1].set_title('Unseperated Laplacian kernel')
plt.show()