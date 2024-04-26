import numpy as np
import matplotlib.pyplot as plt

from p1_convolution import convolution
from p1_normalization import normalization

origin_image = plt.imread('images/origin_images/Figure1.tif')

a = np.array([[-1], [0], [1]])
b = np.array([[1, 2, 1]])

# directions = 

# plt.imshow(origin_image)
# gray image
plt.imshow(origin_image, cmap='gray')
plt.title('origin image')
plt.axis('off')
plt.show()
# plt.savefig('images/p1/p1a.png', dpi=300, bbox_inches='tight')

# origin image, S_x_a, S_x_ab
# origin image, S_y_b, S_y_ba