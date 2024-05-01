clear; clc;

origin_image = imread('../../images/origin_images/blurred.tif');

% N = origin_image.shape(1);
N = size(origin_image, 1);

theta = 124;
d = 16;
L = N / d;

% generate motion blur kernel
H = fspecial('motion', L, theta);
H = psf2otf(H, [N, N]);

% Wiener filter
K = 0.004;
W = conj(H) ./ (abs(H).^2 + K);

% fequency domain of the origin image
F = fft2(origin_image);

% filtering
F_filtered = W .* F;
filtered_image = ifft2(F_filtered);

% show the result
figure;
subplot(1, 2, 1);
imshow(origin_image);
title('origin image');
subplot(1, 2, 2);
imshow(filtered_image, []);
title('restored image');

set(gcf, 'Units', 'Inches');
pos = get(gcf, 'Position');
set(gcf, 'PaperPositionMode', 'Auto', 'PaperUnits', 'Inches', 'PaperSize', [pos(3), pos(4)]);
print(gcf, '../../images/p4/p4c.png', '-dpng', '-r300');