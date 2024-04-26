import numpy as np

# set the negative intensity to 0
# then normalize the image within [0, 255]

def normalization(origin_image: np.array) -> np.array:
    origin_image[origin_image < 0] = 0

    maxn = np.max(np.max(origin_image))
    minn = np.min(np.min(origin_image))
    normalized_image = (origin_image - minn) / (maxn - minn) * 255
    normalized_image = np.uint8(np.round(normalized_image))
    
    return normalized_image