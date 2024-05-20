clear; clc;

sinogram = load('../../images/origin_images/sinogram.mat');
sinogram = sinogram.sinogram;

[n_projections, n_angles] = size(sinogram);

% 1. compute the 1D FFT of each projection.
fft_sinogram = fftshift(fft(sinogram, [], 1), 1);

% employ a Hamming window Ramp filter
Hamming_ramp = abs(ceil(size(sinogram, 1) / 2) - (1:size(sinogram, 1))) / size(sinogram, 1);
Hamming_ramp = Hamming_ramp';

N = size(sinogram, 1);
hamming_function = 0.54 - 0.46 * cos(2 * pi * (0:N-1)' / (N-1));

filter = hamming_function .* Hamming_ramp;
filter = repmat(filter, 1, size(sinogram, 2));

% 2. Multiply the FFT of each projection by the Hamming filter.
filtered_fft_sinogram = fft_sinogram .* filter;

% 3. Obtain the inverse 1D FFT of each resulting filtered transform
filtered_sinogram = real(ifft(ifftshift(filtered_fft_sinogram, 1), [], 1));

% 4. Filtered Back Projection
reconstructed = zeros(n_projections, n_projections);
for i = 1:n_angles
    single_projection = filtered_sinogram(:, i);
    single_projection = repmat(single_projection, 1, n_projections);
    rotated = imrotate(single_projection, -i, 'bilinear', 'crop');
    reconstructed = reconstructed + rotated;
end

% normalize
reconstructed = reconstructed - min(reconstructed(:));
reconstructed = reconstructed / max(reconstructed(:));
normalized = uint8(reconstructed * 255);

% rotate for better visualization
reconstructed = reconstructed';
figure;
imshow(reconstructed);
title('Reconstructed Image');

set(gcf, 'Units', 'Inches');
pos = get(gcf, 'Position');
set(gcf, 'PaperPositionMode', 'Auto', 'PaperUnits', 'Inches', 'PaperSize', [pos(3), pos(4)]);
print(gcf, '../../images/p1/p1.png', '-dpng', '-r300');