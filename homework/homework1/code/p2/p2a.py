import matplotlib.pyplot as plt
import numpy as np
from p2_normalization import normalization
from p2_convolution import convolution

origin_lena = plt.imread('./origin_images/moon.jpg')

# x direction
I_xx = np.array([[1], [-2], [1]])
x_direction = convolution(origin_lena, I_xx)
x_direction = normalization(x_direction)

# y direction
I_yy = np.array([[1, -2, 1]])
y_direction = convolution(origin_lena, I_yy)
y_direction = normalization(y_direction)

Laplacian_kernel = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
unseperated = convolution(origin_lena, Laplacian_kernel)
unseperated = normalization(unseperated)

fig, ax = plt.subplots(1, 3)
ax[0].imshow(x_direction, cmap='gray')
ax[0].set_title('x direction kernel')

ax[1].imshow(y_direction, cmap='gray')
ax[1].set_title('y direction kernel')

ax[2].imshow(unseperated, cmap='gray')
ax[2].set_title('Unseperated Laplacian kernel')
plt.show()