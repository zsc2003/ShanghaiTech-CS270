import numpy as np
import tqdm

def convolution(image: np, kernel: np):
    m, n = kernel.shape

    # zero padding for the image to make sure the output image has the same size as the input image
    image = np.pad(image, pad_width=1, mode='edge')
    w, h = image.shape

    output_w = w - m + 1
    output_h = h - n + 1

    output_image = np.zeros((output_w, output_h), dtype=float)

    for i in tqdm.tqdm(range(output_w)):
        for j in range(output_h):
            output_image[i, j] = np.sum(image[i:i + m, j:j + n] * kernel)

    if m < n:
        output_image = output_image[1:output_w - 1, :]
    elif m > n:
        output_image = output_image[:, 1:output_h - 1]

    return output_image