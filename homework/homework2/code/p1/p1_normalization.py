import numpy as np

# set the negative intensity to 0
# then normalize the image within [0, 255]

def normalization(origin_image: np.array) -> np.array:
    origin_image[origin_image < 0] = 0
    origin_image[origin_image > 255] = 255

    # normalized_image = origin_image
    maxn = np.max(np.max(origin_image))
    minn = np.min(np.min(origin_image))
    minn = 0.0
    normalized_image = (origin_image - minn) / (maxn - minn) * 255

    return normalized_image