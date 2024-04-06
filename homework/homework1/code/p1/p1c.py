import matplotlib.pyplot as plt
import numpy as np
import tqdm
from p1_count_gray_num import count_gray_num

origin_tire = plt.imread('./origin_images/tire.tif')
w, h = origin_tire.shape
patch_size = 41
patch_range = (patch_size - 1) // 2
center_patch_size = 3
center_range = (center_patch_size - 1) // 2
step_size = 1
rate = 0.02
border_line = patch_size * patch_size * rate

output_tire = np.zeros_like(origin_tire, dtype=np.uint8)

# CLAHE
for i in tqdm.tqdm(range(0, w, step_size)):
    for j in range(0, h, step_size):

        # get the patch
        patch = np.zeros((patch_size, patch_size), dtype=np.uint8)
        for x in range(-patch_range, patch_range + 1):
            for y in range(-patch_range, patch_range + 1):
                x_idx = i + x
                y_idx = j + y

                # expand
                if x_idx < 0:
                    x_idx = 0
                elif x_idx >= w:
                    x_idx = w - 1
                if y_idx < 0:
                    y_idx = 0
                elif y_idx >= h:
                    y_idx = h - 1

                patch[x + patch_range, y + patch_range] = origin_tire[x_idx, y_idx]

        # clip the high amplification
        above_border = 0
        gray_num = count_gray_num(patch)

        for k in range(256):
            if gray_num[k] > border_line:
                above_border += gray_num[k] - border_line
                gray_num[k] = border_line
        
        gray_num += above_border / 256
        
        # histogram equalization for the center patch
        prefix_sum = np.cumsum(gray_num) / (patch_size * patch_size)
        prefix_gray = np.round(prefix_sum * 255).astype(np.uint8)

        for x in range(-center_range, center_range + 1):
            for y in range(-center_range, center_range + 1):
                x_idx = i + x
                y_idx = j + y

                # expand
                if x_idx < 0:
                    x_idx = 0
                elif x_idx >= w:
                    x_idx = w - 1
                if y_idx < 0:
                    y_idx = 0
                elif y_idx >= h:
                    y_idx = h - 1

                output_tire[x_idx, y_idx] = prefix_gray[origin_tire[x_idx, y_idx]]

# image after applying CLAHE
fig, ax = plt.subplots(1, 2)
ax[0].imshow(output_tire, cmap='gray')
ax[0].set_title('CLAHE processed image')

# histogram of applyed CIAHE image
gray_num = count_gray_num(output_tire)
ax[1].bar(range(256), gray_num)
ax[1].set_title('histogram of CLAHE processed image')
ax[1].set_xlabel('gray level')
ax[1].set_ylabel('number of pixels')
plt.show()