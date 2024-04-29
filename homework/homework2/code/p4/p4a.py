import numpy as np
import matplotlib.pyplot as plt

origin_image = plt.imread('images/origin_images/blurred.tif').astype(np.float64)

w, h = origin_image.shape
P = 2 ** np.ceil(np.log2(w)).astype(int)
Q = 2 ** np.ceil(np.log2(h)).astype(int)

# times (-1) ** (u + v) before FFT for shifting
image_for_shift = origin_image * (-1) ** (np.arange(w).reshape(-1, 1) + np.arange(h))

# FFT
image_fft_shift = np.fft.fft2(image_for_shift, (P, Q))

# show frequency domain
image_fft_shift_abs = np.abs(image_fft_shift)
plt.imshow(20 * np.log(1 + image_fft_shift_abs), cmap='gray')
plt.title('Frequency domain')
plt.axis('off')
plt.savefig('images/p4/p4a.png', dpi=300, bbox_inches='tight')
