import numpy as np
import matplotlib.pyplot as plt

def generate_frequency_image(origin_image):
    w, h = origin_image.shape

    # times (-1) ** (u + v) before FFT for shifting
    image_for_shift = origin_image * (-1) ** (np.arange(w).reshape(-1, 1) + np.arange(h))

    # FFT
    image_fft_shift = np.fft.fft2(image_for_shift)

    # show frequency domain
    image_fft_shift_abs = 20 * np.log(100 + np.abs(image_fft_shift))

    return image_fft_shift_abs

if __name__ == '__main__':
    origin_image = plt.imread('images/origin_images/blurred.tif').astype(np.float64)
    image_fft_shift_abs = generate_frequency_image(origin_image)

    plt.imshow(image_fft_shift_abs, cmap='gray')
    plt.title('Frequency domain')
    plt.axis('off')
    plt.savefig('images/p4/p4a.png', dpi=300, bbox_inches='tight')