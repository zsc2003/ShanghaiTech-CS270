from typing import List
import numpy as np

# count the number of each pixel value
def count_gray_num(origin_image: np.array) -> np.array:
    gray_num = np.zeros(256, dtype=float)
    w, h = origin_image.shape

    for i in range(w):
        for j in range(h):
            gray_num[int(origin_image[i][j])] += 1
    
    return gray_num