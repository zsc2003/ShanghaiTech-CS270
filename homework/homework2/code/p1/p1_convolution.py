import numpy as np
import tqdm

def convolution(image: np, kernel: np):
    w, h = image.shape
    m, n = kernel.shape

    x_size = m // 2
    y_size = n // 2

    # zero padding for the image to make sure the output image has the same size as the input image
    image = np.pad(image, ((x_size, x_size), (y_size, y_size)), 'constant', constant_values=(0, 0))

    w, h = image.shape

    new_image = np.zeros((w, h), dtype=float)
    for i in tqdm.tqdm(range(x_size, w - x_size)):
        for j in range(y_size, h - y_size):
            sum = 0
            for s in range(-x_size, x_size + 1):
                for t in range(-y_size, y_size + 1):
                    sum += kernel[s + x_size, t + y_size] * image[i - s, j - t]
            new_image[i, j] = sum
    
    # ignore the padding part
    new_image = new_image[x_size:w - x_size, y_size:h - y_size]
    return new_image