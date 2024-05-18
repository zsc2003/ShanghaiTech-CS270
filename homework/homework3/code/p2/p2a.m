clear; clc;

image = imread('../../images/origin_images/flower.tif');

intensity1 = double(image(:, :, 1)) / 3 + double(image(:, :, 2)) / 3 + double(image(:, :, 3)) / 3;
intensity1 = intensity1 / 256;

intensity2 = double(rgb2gray(image)) / 256;
foreground1 = global_thresholding(image, intensity1);
foreground2 = global_thresholding(image, intensity2);

figure;
imshow(image);
title('Original Image');
set(gcf, 'Units', 'Inches');
pos = get(gcf, 'Position');
set(gcf, 'PaperPositionMode', 'Auto', 'PaperUnits', 'Inches', 'PaperSize', [pos(3), pos(4)]);
print(gcf, '../../images/p2/p2a_origin.png', '-dpng', '-r300');

% show the results
figure;
subplot(2, 2, 1);
histogram(intensity1, 256);
title('Histogram of Intensity 1');

subplot(2, 2, 2);
histogram(intensity2, 256);
title('Histogram of Intensity 2');

subplot(2, 2, 3);
imshow(uint8(foreground1));
title('Foreground Image 1');
subplot(2, 2, 4);
imshow(uint8(foreground2));
title('Foreground Image 2');

set(gcf, 'Units', 'Inches', 'Position', [0, 0, 10, 10]);
pos = get(gcf, 'Position');
set(gcf, 'PaperPositionMode', 'Auto', 'PaperUnits', 'Inches', 'PaperSize', [pos(3), pos(4)]);
print(gcf, '../../images/p2/p2a_result.png', '-dpng', '-r300');


function result = global_thresholding(origin_image, intensity)
    T = 0.1;
    new_T = 0.1;

    while true
        mask = intensity > T;

        G1 = intensity .* double(mask);
        G2 = intensity .* double(~mask);

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

    result = zeros(size(origin_image));
    foreground = intensity > T;
    for i = 1:3
        result(:, :, i) = origin_image(:, :, i) .* uint8(foreground);
    end
end