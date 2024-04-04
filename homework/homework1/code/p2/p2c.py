import matplotlib.pyplot as plt
import numpy as np
from p2_normalization import normalization
from p2_convolution import convolution

origin_moon = plt.imread('./origin_images/moon.jpg')
w, h = origin_moon.shape


# two types of smoothing filter for blurring the origin image
smooth_filter = [np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]]) / 9, np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]]) / 16]

# do not drop < 0 parts
for i, filter in enumerate(smooth_filter):

    fig, ax = plt.subplots(1, 5)
    # blurred image
    smoothed_moon = convolution(origin_moon, filter)
    ax[0].imshow(normalization(smoothed_moon), cmap='gray')
    ax[0].set_title('smoothed moon with filter ' + str(i + 1))
    
    # unsharp image
    unsharp_mask = origin_moon - smoothed_moon
    ax[1].imshow(normalization(unsharp_mask), cmap='gray')
    ax[1].set_title('unsharp mask')


    for j, k in enumerate([1.0, 4.5]):
        # sharpened image
        sharpened_moon = origin_moon + k * unsharp_mask
        ax[2 + j].imshow(normalization(sharpened_moon), cmap='gray')
        ax[2 + j].set_title('sharpened moon with k = ' + str(k))

    ax[4].imshow(origin_moon, cmap='gray')
    ax[4].set_title('origin image')
    
    plt.show()

# drop < 0 and > 255 parts
for i, filter in enumerate(smooth_filter):

    fig, ax = plt.subplots(1, 5)
    # blurred image
    smoothed_moon = convolution(origin_moon, filter)
    ax[0].imshow(normalization(smoothed_moon), cmap='gray')
    ax[0].set_title('smoothed moon with filter ' + str(i + 1))
    
    # unsharp image
    unsharp_mask = origin_moon - smoothed_moon
    ax[1].imshow(np.minimum(np.maximum(unsharp_mask, 0), 255), cmap='gray')
    ax[1].set_title('unsharp mask')


    for j, k in enumerate([1.0, 4.5]):
        # sharpened image
        sharpened_moon = origin_moon + k * unsharp_mask
        ax[2 + j].imshow(np.minimum(np.maximum(sharpened_moon, 0), 255), cmap='gray')
        ax[2 + j].set_title('sharpened moon with k = ' + str(k))

    ax[4].imshow(origin_moon, cmap='gray')
    ax[4].set_title('origin image')
    
    plt.show()