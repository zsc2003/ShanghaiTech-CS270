import numpy as np
import matplotlib.pyplot as plt
from p1_normalization import normalization

def distance_square(P, Q):
    # D_square = (i - P // 2) ** 2 + (j - Q // 2) ** 2)
    i = np.arange(P)
    j = np.arange(Q)
    I, J = np.meshgrid(i, j)
    D_square = (I - P // 2) ** 2 + (J - Q // 2) ** 2
    return D_square

def Gaussian_high_pass_filter(P, Q, D0):
    H = 1 - np.exp(-distance_square(P, Q) / (2 * D0 ** 2))
    return H

def show_Gaussian(P, Q, H):
    # show the Gaussian high pass filter
    plt.figure()
    plt.imshow(H, cmap='gray')
    plt.title('Gaussian high pass filter')
    plt.savefig('images/p1/p1b_Gaussian.png', dpi=300, bbox_inches='tight')

    # show the gaussian high pass filter in 3D
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    x = np.arange(P)
    y = np.arange(Q)
    X, Y = np.meshgrid(x, y)
    ax.plot_surface(X, Y, H, cmap='viridis')
    plt.title('Gaussian high pass filter in 3D view')
    plt.savefig('images/p1/p1b_Gaussian_3D.png', dpi=300, bbox_inches='tight')

def show_filter(origin_image, origin_image_fft_shift, origin_image_fft_shift_filtered, origin_image_filtered):
    fig, axs = plt.subplots(2, 2)
    fig.subplots_adjust(hspace=0.4, wspace=0.0)

    axs[0, 0].imshow(origin_image, cmap='gray')
    axs[0, 0].set_title('origin image')

    axs[0, 1].imshow(normalization(20 * np.log(1 + np.abs(origin_image_fft_shift))), cmap='gray')
    axs[0, 1].set_title('origin image frequency domain')

    axs[1, 0].imshow(normalization(20 * np.log(1 + np.abs(origin_image_fft_shift_filtered))), cmap='gray')
    axs[1, 0].set_title('filtered image frequency domain')

    axs[1, 1].imshow(normalization(origin_image_filtered), cmap='gray')
    axs[1, 1].set_title('filtered image')

    plt.savefig('images/p1/p1b_filter.png', dpi=300, bbox_inches='tight')


origin_image = plt.imread('images/origin_images/Figure1.tif')

w, h = origin_image.shape

# power of 2 for FFT
P = 2 ** np.ceil(np.log2(w)).astype(int)
Q = 2 ** np.ceil(np.log2(h)).astype(int)

# use Gaussian high pass filter to enhance the image
D0 = 100
H = Gaussian_high_pass_filter(P, Q, D0)

show_Gaussian(P, Q, H)

# FFT
origin_image_fft = np.fft.fft2(origin_image, s=(P, Q))
origin_image_fft_shift = np.fft.fftshift(origin_image_fft)

# apply the Gaussian high pass filter
origin_image_fft_shift_filtered = origin_image_fft_shift * H

# IFFT
origin_image_fft_filtered = np.fft.ifftshift(origin_image_fft_shift_filtered)
origin_image_filtered = np.fft.ifft2(origin_image_fft_filtered)
origin_image_filtered = np.real(origin_image_filtered)

# crop the image
origin_image_filtered = origin_image_filtered[:w, :h]

show_filter(origin_image, origin_image_fft_shift, origin_image_fft_shift_filtered, origin_image_filtered)