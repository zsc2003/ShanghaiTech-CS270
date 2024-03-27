clear;clc;

origin_moon = imread('../../origin_images/moon.jpg');
[w, h] = size(origin_moon);

blurred_moon = double(origin_moon);
moon_average = sum(sum(blurred_moon)) / (w * h);
blurred_moon = blurred_moon - moon_average;







% normalize the blurred_moon within [0, 255]
maxn = max(max(blurred_moon));
minn = min(min(blurred_moon));
blurred_moon = (blurred_moon - minn) / (maxn - minn) * 255;
blurred_moon = uint8(round(blurred_moon));






figure(1);
imshow(blurred_moon);