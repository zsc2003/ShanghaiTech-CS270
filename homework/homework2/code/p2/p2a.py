import numpy as np
import matplotlib.pyplot as plt
from p2_normalization import normalization


def distance_square(P, Q):
    # D_square = (i - P // 2) ** 2 + (j - Q // 2) ** 2)
    i = np.arange(P)
    j = np.arange(Q)
    J, I = np.meshgrid(j, i)
    D_square = (I - P // 2) ** 2 + (J - Q // 2) ** 2
    return D_square

def generate_filter(P, Q, D0, gamma_l, gamma_h, c):
    D_square = distance_square(P, Q)
    H = (gamma_h - gamma_l) * (1 - np.exp(-c * D_square / (D0 ** 2))) + gamma_l
    return H

def show_filter(P, Q, H):
    # show the Gaussian high pass filter
    plt.figure()
    plt.imshow(H, cmap='gray')
    plt.title('Gaussian high pass filter')
    plt.savefig('images/p2/p2a_filter.png', dpi=300, bbox_inches='tight')

    # show the gaussian high pass filter in 3D
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    y = np.arange(P)
    x = np.arange(Q)
    X, Y = np.meshgrid(x, y)
    ax.plot_surface(X, Y, H, cmap='viridis')
    plt.title('Gaussian high pass filter in 3D view')
    plt.savefig('images/p2/p2a_filter_3D.png', dpi=300, bbox_inches='tight')

# apply homomorphic filtering
def homomorphic_filtering(image, P, Q, gamma_l=0.5, gamma_h=2.0, c=1, D0=80):
    w, h = image.shape
    epsilon = 1
    ln_image = np.log(epsilon + image)

    # FFT
    ln_image_fft = np.fft.fft2(ln_image, (P, Q))
    ln_image_fft_shift = np.fft.fftshift(ln_image_fft)

    # generate filter
    H = generate_filter(P, Q, D0, gamma_l, gamma_h, c)
    show_filter(P,Q,H)

    # filtering
    ln_image_fft_shift_filtered = ln_image_fft_shift * H
    ln_image_fft_filtered = np.fft.ifftshift(ln_image_fft_shift_filtered)
    image_filtered = np.fft.ifft2(ln_image_fft_filtered)
    image_filtered = np.real(image_filtered)
    image_filtered = image_filtered[:w, :h]
    image_filtered = np.exp(image_filtered) - epsilon
    image_filtered = normalization(image_filtered)

    return image_filtered

def show_result(origin_image, filtered_image):
    # clear the figure
    plt.clf()
    
    plt.subplot(1, 2, 1)
    plt.imshow(origin_image, cmap='gray')
    plt.title('origin image')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(filtered_image, cmap='gray')
    plt.title('filtered image')
    plt.axis('off')

    plt.savefig('images/p2/p2a_result.png', dpi=300, bbox_inches='tight')


origin_image = plt.imread('images/origin_images/PET-scan.tif').astype(float)

w, h = origin_image.shape

# power of 2 for FFT
P = 2 ** np.ceil(np.log2(w)).astype(int)
Q = 2 ** np.ceil(np.log2(h)).astype(int)

filtered_image = homomorphic_filtering(origin_image, P, Q)
print('variance of origin image in region [500~1100, 90~180] is : ', np.var(filtered_image[500:1101, 90:181]))

show_result(origin_image, filtered_image)