import matplotlib.pyplot as plt
import numpy as np
from p2_normalization import normalization
from p2_convolution import convolution

origin_moon = plt.imread('./origin_images/moon.jpg')
plt.imshow(origin_moon, cmap='gray')
plt.title('origin moon')
plt.show()

w, h = origin_moon.shape

# two types of smoothing filter for blurring the origin image
smooth_filter = [np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]]) / 9, np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]]) / 16]
for i, filter in enumerate(smooth_filter):
    # blurred image
    smoothed_moon = convolution(origin_moon, filter)
    plt.imshow(normalization(smoothed_moon), cmap='gray')
    plt.title('smoothed moon with filter ' + str(i + 1))
    plt.show()
    
    # unsharp image
    unsharp_mask = origin_moon - smoothed_moon
    plt.imshow(normalization(unsharp_mask), cmap='gray')
    plt.title('unsharp mask')
    plt.show()

    for k in [1.0, 4.5]:
        # sharpened image
        sharpened_moon = origin_moon + k * unsharp_mask
        plt.imshow(sharpened_moon, cmap='gray')
        plt.title('sharpened moon with k = ' + str(k))
        plt.show()