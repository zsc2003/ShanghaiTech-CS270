clear;clc;

origin_grain = imread('../../origin_images/grain.tif');
gray_num = p1_count_gray_num(origin_grain);

% plot the histogram
figure(1);
bar(0:255, gray_num);
xlabel('gray level');
ylabel('number of pixels');
title('histogram of grain.tif');