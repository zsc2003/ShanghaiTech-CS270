import numpy as np
import matplotlib.pyplot as plt

from p1_convolution import convolution
from p1_normalization import normalization

def show_res(origin_image, S_x_a, S_x_ab, S_y_b, S_y_ba):
    fig, axs = plt.subplots(2, 3)
    fig.subplots_adjust(hspace=0, wspace=0.1)

    axs[0, 0].imshow(origin_image, cmap='gray')
    axs[0, 0].set_title('origin image')
    axs[0, 0].axis('off')

    axs[0, 1].imshow(normalization(S_x_a), cmap='gray')
    axs[0, 1].set_title('S_x_a')
    axs[0, 1].axis('off')

    axs[0, 2].imshow(normalization(S_x_ab), cmap='gray')
    axs[0, 2].set_title('S_x_ab')
    axs[0, 2].axis('off')

    axs[1, 0].imshow(origin_image, cmap='gray')
    axs[1, 0].set_title('origin image')
    axs[1, 0].axis('off')

    axs[1, 1].imshow(normalization(S_y_b), cmap='gray')
    axs[1, 1].set_title('S_y_b')
    axs[1, 1].axis('off')

    axs[1, 2].imshow(normalization(S_y_ba), cmap='gray')
    axs[1, 2].set_title('S_y_ba')
    axs[1, 2].axis('off')
    
    plt.savefig('images/p1/p1a.png', dpi=300, bbox_inches='tight')

origin_image = plt.imread('images/origin_images/Figure1.tif')

a = np.array([[-1], [0], [1]])
b = np.array([[1], [2], [1]])

S_x_a = convolution(origin_image, a)
S_x_ab = convolution(S_x_a, b.T)

S_y_b = convolution(origin_image, b)
S_y_ba = convolution(S_y_b, a.T)

show_res(origin_image, S_x_a, S_x_ab, S_y_b, S_y_ba)