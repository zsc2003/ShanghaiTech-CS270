import matplotlib.pyplot as plt
import numpy as np
from p2_normalization import normalization
from p2_convolution import convolution

origin_lena = plt.imread('./origin_images/moon.jpg')

# x direction
I_xx = np.array([[1, -2, 1]])
x_direction = convolution(origin_lena, I_xx)
x_direction = normalization(x_direction)
plt.imshow(x_direction, cmap='gray')
plt.title('x direction kernel')
plt.show()

# y direction
I_yy = np.array([[1], [-2], [1]])
y_direction = convolution(origin_lena, I_yy)
y_direction = normalization(y_direction)
plt.imshow(y_direction, cmap='gray')
plt.title('y direction kernel')
plt.show()