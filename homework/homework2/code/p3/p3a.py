import numpy as np
import matplotlib.pyplot as plt

def RGB2HSI(RGB_image):
    R = RGB_image[:, :, 0].astype(np.float32)
    G = RGB_image[:, :, 1].astype(np.float32)
    B = RGB_image[:, :, 2].astype(np.float32)

    # set up a epsilon to avoid divide by zero
    epsilon = 1e-9

    value = (0.5 * ((R - G) + (R - B))) / (np.sqrt((R - G) ** 2 + (R - B) * (G - B) ) + epsilon)

    # clip to make sure arccos has no nan
    theta = np.arccos(np.clip(value, -1, 1))

    # convert RGB to HSI
    H = theta.copy()
    H[G < B] = 2 * np.pi - H[G < B]
    S = 1 - 3 * np.minimum(np.minimum(R, G), B) / (R + G + B + epsilon)
    I = (R + G + B) / 3

    # normalize all channels to [0, 1] in HSI space
    H = H / (2 * np.pi)
    S /= 1
    I /= 255

    HSI_image = np.stack((H, S, I), axis=2)
    return HSI_image

def HSI2RGB(HSI_image):
    H = HSI_image[:, :, 0].astype(np.float32)
    S = HSI_image[:, :, 1].astype(np.float32)
    I = HSI_image[:, :, 2].astype(np.float32)

    H *= 2 * np.pi
    S *= 1
    I *= 255

    numerator = np.where(H < 2 * np.pi / 3, np.cos(H), np.where(H < 4 * np.pi / 3, np.cos(H - 2 * np.pi / 3), np.cos(H - 4 * np.pi / 3)))
    denominator = np.where(H < 2 * np.pi / 3, np.cos(np.pi / 3 - H), np.where(H < 4 * np.pi / 3, np.cos(np.pi - H), np.cos(5 * np.pi / 3 - H)))

    value_1 = I * (1 - S)
    value_2 = I * (1 + S * numerator / denominator)
    value_3 = 3 * I - (value_1 + value_2)

    R = np.where(H < 2 * np.pi / 3, value_2, np.where(H < 4 * np.pi / 3, value_1, value_3))
    G = np.where(H < 2 * np.pi / 3, value_3, np.where(H < 4 * np.pi / 3, value_2, value_1))
    B = np.where(H < 2 * np.pi / 3, value_1, np.where(H < 4 * np.pi / 3, value_3, value_2))

    recovery_RGB = np.stack((R, G, B), axis=2)
    recovery_RGB = np.clip(recovery_RGB, 0, 255).astype(np.uint8)
    return recovery_RGB


origin_image = plt.imread('images/origin_images/PeppersRGB.jpg')
HSI_image = RGB2HSI(origin_image)
recovery_RGB = HSI2RGB(HSI_image)

plt.subplot(1, 3, 1)
plt.imshow(origin_image)
plt.title('RGB image')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(HSI_image)
plt.title('HSI image')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(recovery_RGB)
plt.title('Recovery RGB image')
plt.axis('off')

plt.savefig('images/p3/p3.png', dpi=300, bbox_inches='tight')