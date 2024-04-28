import numpy as np
import matplotlib.pyplot as plt


def distance_square(P, Q):
    # D_square = (i - P // 2) ** 2 + (j - Q // 2) ** 2)
    i = np.arange(P)
    j = np.arange(Q)
    I, J = np.meshgrid(i, j)
    D_square = (I - P // 2) ** 2 + (J - Q // 2) ** 2
    return D_square

def generate_filter(P, Q, D0, gamma_l, gamma_h, c):
    D_square = distance_square(P, Q)
    H = (gamma_h - gamma_l) * (1 - np.exp(-c * D_square / (D0 ** 2))) + gamma_l
    return H

# apply homomorphic filtering
def homomorphic_filtering(image, D, gamma_l, gamma_h, c, D0):
    pass




origin_image = plt.imread('images/origin_images/PET-scan.tif')

w, h = origin_image.shape


# power of 2 for FFT
P = 2 ** np.ceil(np.log2(w)).astype(int)
Q = 2 ** np.ceil(np.log2(h)).astype(int)

print(w,h,P,Q)
exit()


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

