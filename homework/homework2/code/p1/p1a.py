import numpy as np
import matplotlib.pyplot as plt

from p1_convolution import convolution
from p1_normalization import normalization

def show_res(origin_image, S_x_a, S_x_ab, S_y_b, S_y_ba, sharpened_x, sharpened_y):
    fig, axs = plt.subplots(2, 4)
    fig.subplots_adjust(hspace=0)
    
    axs[0, 0].imshow(origin_image, cmap='gray')
    axs[0, 0].set_title('origin image')
    axs[0, 0].axis('off')

    axs[0, 1].imshow(normalization(S_x_a), cmap='gray')
    axs[0, 1].set_title('S_x_a')
    axs[0, 1].axis('off')

    axs[0, 2].imshow(normalization(S_x_ab), cmap='gray')
    axs[0, 2].set_title('S_x_ab')
    axs[0, 2].axis('off')

    axs[0, 3].imshow(normalization(sharpened_x), cmap='gray')
    axs[0, 3].set_title('sharpened image')
    axs[0, 3].axis('off')

    axs[1, 0].imshow(origin_image, cmap='gray')
    axs[1, 0].set_title('origin image')
    axs[1, 0].axis('off')

    axs[1, 1].imshow(S_y_b, cmap='gray')
    axs[1, 1].set_title('S_y_b')
    axs[1, 1].axis('off')

    axs[1, 2].imshow(normalization(S_y_ba), cmap='gray')
    axs[1, 2].set_title('S_y_ba')
    axs[1, 2].axis('off')

    axs[1, 3].imshow(normalization(sharpened_y), cmap='gray')
    axs[1, 3].set_title('sharpened image')
    axs[1, 3].axis('off')
    
    plt.savefig('images/p1/p1a.png', dpi=300, bbox_inches='tight')

    gradient = np.sqrt(S_x_ab ** 2 + S_y_ba ** 2)

    fig, axs = plt.subplots(1, 2)

    axs[0].imshow((gradient), cmap='gray')
    axs[0].set_title('gradient')

    axs[1].imshow(normalization((gradient) + origin_image), cmap='gray')
    axs[1].set_title('sharpened image by gradient')   
    plt.savefig('images/p1/p1a_gradient.png', dpi=300, bbox_inches='tight')

if __name__ == '__main__':
    origin_image = plt.imread('images/origin_images/Figure1.tif')

    a = np.array([[-1], [0], [1]])
    b = np.array([[1], [2], [1]])

    S_x_a = convolution(origin_image, a)
    S_x_ab = convolution(S_x_a, b.T)

    S_y_b = convolution(origin_image, b)
    S_y_ba = convolution(S_y_b, a.T)

    sharpened_x = origin_image + normalization(S_x_ab)
    sharpened_y = origin_image + normalization(S_y_ba)

    show_res(origin_image, S_x_a, S_x_ab, S_y_b, S_y_ba, sharpened_x, sharpened_y)