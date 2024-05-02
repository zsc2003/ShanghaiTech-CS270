import numpy as np
import matplotlib.pyplot as plt
from p4a import generate_frequency_image

from scipy.ndimage import rotate
from skimage.transform import radon

import warnings
warnings.filterwarnings('ignore')


if __name__ == '__main__':
    origin_image = plt.imread('images/origin_images/blurred.tif')
    frequency_image = generate_frequency_image(origin_image)
    N = frequency_image.shape[0]

    sinogram = radon(frequency_image, circle=False)
    plt.figure()
    plt.imshow(sinogram, cmap='gray')
    plt.title('Radon transform')
    plt.xlabel('Angle (degrees)')
    plt.ylabel('rho')
    plt.yticks([0, 53, 153, 253, 353, 453, 553, 653, 753, 853, 906], [-453, -400, -300, -200, -100, 0, 100, 200, 300, 400, 453])
    plt.savefig('images/p4/p4b_radon.png')

    # theta is the angle of the x-coordinate of the Radon image's maximum value
    max_value = np.max(sinogram)
    max_index = np.where(sinogram == max_value)
    theta = max_index[1][0]
    print(f'The estimated motion blur angle is {theta} degrees')

    # Rotate the image to the estimated angle
    rotated_image = rotate(frequency_image, 180-theta, reshape=False)
    plt.figure()
    plt.imshow(rotated_image, cmap='gray')
    plt.title('Rotated spectrum')
    plt.axis('off')
    plt.savefig('images/p4/p4b_rotated_image.png')

    # get the intensity on the x-axis of rho = 0
    rho = 0
    # intensity = rotated_image[N//2, :]
    intensity = np.sum(rotated_image, axis=0)
    plt.figure()
    plt.plot(intensity)
    plt.title('Verticle projection')
    plt.xlabel('x-axis')
    plt.ylabel('Intensity')
    plt.xticks([0, 20, 120, 220, 320, 420, 520, 620, 640], [' ', -300, -200, -100, 0, 100, 200, 300, ' '])
    plt.savefig('images/p4/p4b_intensity.png')

    # get the motion blur length
    max_value = np.max(intensity)
    max_index = np.where(intensity == max_value)[0][0]
    local_minima = max_index
    for i in range(max_index, len(intensity)):
        if intensity[i - 2] > intensity[i - 1] and intensity[i - 1] > intensity[i] and intensity[i + 1] > intensity[i] and intensity[i + 1] < intensity[i + 2] and intensity[i + 2] < intensity[i + 3]:
            local_minima = i
            break
    
    d = local_minima - max_index
    print(f'The distance between the two similar dark stripes is {d}')