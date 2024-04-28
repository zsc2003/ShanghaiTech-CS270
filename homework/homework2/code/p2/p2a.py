import numpy as np
import matplotlib.pyplot as plt


def distance_square(P, Q):
    # D_square = (i - P // 2) ** 2 + (j - Q // 2) ** 2)
    i = np.arange(P)
    j = np.arange(Q)
    J, I = np.meshgrid(j, i)
    D_square = (I - P // 2) ** 2 + (J - Q // 2) ** 2
    print('D_square:', D_square.shape)
    return D_square

def generate_filter(P, Q, D0, gamma_l, gamma_h, c):
    D_square = distance_square(P, Q)
    H = (gamma_h - gamma_l) * (1 - np.exp(-c * D_square / (D0 ** 2))) + gamma_l
    return H

# apply homomorphic filtering
def homomorphic_filtering(image, P, Q, gamma_l=0.5, gamma_h=2.0, c=4, D0=10):
    epsilon = 1e-9
    ln_image = np.log(epsilon + image)
    print(image.shape)

    # FFT
    ln_image_fft = np.fft.fft2(ln_image, (P, Q))
    print(ln_image_fft.shape)
    ln_image_fft_shift = np.fft.fftshift(ln_image_fft)
    print(ln_image_fft_shift.shape)

    # generate filter
    H = generate_filter(P, Q, D0, gamma_l, gamma_h, c)
    # filtering
    ln_image_fft_shift_filtered = ln_image_fft_shift * H
    ln_image_fft_filtered = np.fft.ifftshift(ln_image_fft_shift_filtered)
    image_filtered = np.fft.ifft2(ln_image_fft_filtered)
    image_filtered = np.real(image_filtered)

    return np.exp(image_filtered)




origin_image = plt.imread('images/origin_images/PET-scan.tif').astype(float)

w, h = origin_image.shape

# power of 2 for FFT
P = 2 ** np.ceil(np.log2(w)).astype(int)
Q = 2 ** np.ceil(np.log2(h)).astype(int)

filtered_image = homomorphic_filtering(origin_image, P, Q)

# plot the images
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(origin_image, cmap='gray')
plt.title('origin image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(filtered_image, cmap='gray')
plt.title('filtered image')
plt.axis('off')

plt.show()
# plt.savefig('images/p2/p2a.png', dpi=300, bbox_inches='tight')









# plt.imshow(origin_image)
# plt.title('origin image')
# plt.axis('off')

# plt.show()
# plt.savefig('images/p2/p2a.png', dpi=300, bbox_inches='tight')

