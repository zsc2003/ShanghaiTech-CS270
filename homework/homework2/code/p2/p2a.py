import numpy as np
import matplotlib.pyplot as plt


def distance_square(P, Q):
    # D_square = (i - P // 2) ** 2 + (j - Q // 2) ** 2)
    i = np.arange(P)
    j = np.arange(Q)
    I, J = np.meshgrid(i, j)
    D_square = (I - P // 2) ** 2 + (J - Q // 2) ** 2
    return D_square

# apply homomorphic filtering
def homomorphic_filtering(image, D, gamma_l=0.5, gamma_h=0.6, c=1, D0=50):
    # get the shape of the image
    rows, cols = image.shape

    # create the filter
    H = (gamma_h - gamma_l) * [1 - np.exp ** (-c * (D / D0) ** 2) + gamma_l]
    filter = np.zeros((rows, cols))

    for i in range(rows):
        for j in range(cols):
            filter[i, j] = (gamma_h - gamma_l) * (1 - np.exp(-c * ((i - rows / 2) ** 2 + (j - cols / 2) ** 2) / (D0 ** 2))) + gamma_l

    # apply the filter to the image
    # filtered_image = np.fft.ifftshift(np.fft.ifft2(np.fft.fft2(image) * filter)).real
    filtered_image = (np.fft.ifft2(np.fft.fft2(image) * filter)).real

    return filtered_image




origin_image = plt.imread('images/origin_images/PET-scan.tif')

w, h = origin_image.shape

# power of 2 for FFT
P = 2 ** np.ceil(np.log2(w)).astype(int)
Q = 2 ** np.ceil(np.log2(h)).astype(int)

filtered_image = homomorphic_filtering(origin_image)

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

