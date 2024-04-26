import numpy as np
import matplotlib.pyplot as plt

origin_image = plt.imread('images/origin_images/PeppersRGB.jpg')

R = origin_image[:, :, 0].astype(np.float32)
G = origin_image[:, :, 1].astype(np.float32)
B = origin_image[:, :, 2].astype(np.float32)

# set up a epsilon to avoid divide by zero
epsilon = 1e-9

value = (0.5 * ((R - G) + (R - B))) / (np.sqrt((R - G) ** 2 + (R - B) * (G - B) ) + epsilon)

# clip to make sure arccos has no nan
theta = np.arccos(np.clip(value, -1, 1))

# np.arccos return value in [0, pi], convert in [0, 180]
theta = theta / np.pi * 180

# convert RGB to HSI
H = theta.copy()
H[G < B] = 360 - H[G < B]
S = 1 - 3 * np.minimum(np.minimum(R, G), B) / (R + G + B+ epsilon)
I = (R + G + B) / 3

# normalize all channels to [0, 1] in HSI space
H /= 360
S /= 1
I /= 255
HSI_image = np.stack((H, S, I), axis=2)

plt.subplot(1, 2, 1)
plt.imshow(origin_image)
plt.title('origin image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(HSI_image)
plt.title('HSI image')
plt.axis('off')

plt.savefig('images/p3/p3.png', dpi=300, bbox_inches='tight')