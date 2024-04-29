import numpy as np

# set the negative intensity to 0
# then normalize the image within [0, 1]

def normalization(origin_image: np.array) -> np.array:
    origin_image[origin_image < 0] = 0

    maxn = np.max(np.max(origin_image)).astype(float)
    minn = np.min(np.min(origin_image)).astype(float)
    normalized_image = (origin_image - minn) / (maxn - minn)
    
    return normalized_image