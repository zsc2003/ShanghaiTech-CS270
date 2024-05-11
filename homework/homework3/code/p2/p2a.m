clear; clc;

image = imread('../../images/origin_images/flower.tif');

figure;
imshow(image);
title('Original Image');


% set(gcf, 'Units', 'Inches');
% pos = get(gcf, 'Position');
% set(gcf, 'PaperPositionMode', 'Auto', 'PaperUnits', 'Inches', 'PaperSize', [pos(3), pos(4)]);
% print(gcf, '../../images/p3/p3.png', '-dpng', '-r300');