import numpy as np
import matplotlib.pyplot as plt
from p4a import generate_frequency_image
from scipy.ndimage import rotate
import tqdm

def radon_transform(image, num_angles=180):
    angles = np.linspace(0, 180, num_angles, endpoint=False)
    sinogram = np.zeros((num_angles, image.shape[1]))
    for i, angle in tqdm.tqdm(enumerate(angles)):
        # 旋转图像
        rotated_image = rotate(image, angle, reshape=False, order=1, mode='nearest')
        # 计算垂直方向的投影
        projection = np.sum(rotated_image, axis=0)
        sinogram[i, :] = projection
    return sinogram

origin_image = plt.imread('images/origin_images/blurred.tif')
frequency_image = generate_frequency_image(origin_image)
N = frequency_image.shape[0]

# 计算 Radon 变换
radon_image = radon_transform(frequency_image)

# 显示结果
plt.imshow(radon_image, cmap='gray')
plt.title('Radon Transform')
plt.axis('off')
plt.show()

# 找到 Radon 图像中的最大值
max_value = np.max(radon_image)
max_index = np.where(radon_image == max_value)
angle_index = max_index[0][0]  # 获取角度索引
angles = np.linspace(0, 180, radon_image.shape[0], endpoint=False)
angle = angles[angle_index]  # 获取估计的角度

print('The estimated motion blur angle is', angle, 'degrees')

# 估计相似暗条纹之间的距离
# 计算两个最大值之间的距离
def estimate_distance(sinogram):
    # 假设我们知道条纹是在最亮的线上
    brightest_row = sinogram[np.argmax(np.sum(sinogram, axis=1))]
    peaks = np.where(brightest_row > np.max(brightest_row) * 0.8)[0]
    if len(peaks) > 1:
        return np.min(np.diff(peaks))
    else:
        return None

distance = estimate_distance(radon_image)
if distance:
    print('Estimated distance between stripes:', distance)
else:
    print('Could not estimate distance - not enough peaks detected.')