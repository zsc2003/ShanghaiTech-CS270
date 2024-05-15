clear; clc;

image = imread('../../images/origin_images/flower.tif');


intensity = double(image(:, :, 1)) / 3 + double(image(:, :, 2)) / 3 + double(image(:, :, 3)) / 3;
intensity = intensity / 256;

% show the histogram of the intensity
figure;
histogram(intensity, 256);
title('Histogram of Intensity');
set(gcf, 'Units', 'Inches');
pos = get(gcf, 'Position');
set(gcf, 'PaperPositionMode', 'Auto', 'PaperUnits', 'Inches', 'PaperSize', [pos(3), pos(4)]);
print(gcf, '../../images/p2/p2a_intensity.png', '-dpng', '-r300');

T = 0.1;
new_T = 0.1;

while true
    mask = intensity > T;

    G1 = intensity .* double(mask);
    G2 = intensity .* double(~mask);

    % m1 = mean(G1(:))
    % m2 = mean(G2(:))
    % get the mean of non-zero elements
    m1 = sum(G1(:)) / sum(mask(:));
    m2 = sum(G2(:)) / sum(~mask(:));

    new_T = (m1 + m2) / 2;

    % convergence
    if abs(T - new_T) < 0.00001
        break;
    end
    T = new_T;
end

result = zeros(size(image));
forward = intensity > T;
for i = 1:3
    result(:, :, i) = image(:, :, i) .* uint8(forward);
end


figure;
subplot(1, 2, 1);
imshow(image);
title('Original Image');
subplot(1, 2, 2);
imshow(uint8(result));
title('Foreground Image');

set(gcf, 'Units', 'Inches');
pos = get(gcf, 'Position');
set(gcf, 'PaperPositionMode', 'Auto', 'PaperUnits', 'Inches', 'PaperSize', [pos(3), pos(4)]);
print(gcf, '../../images/p2/p2a_result.png', '-dpng', '-r300');