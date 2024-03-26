origin_moon = imread('../origin_images/moon.jpg');
[w, h] = size(origin_moon);

blurred_moon = double(origin_moon);
moon_average = sum(sum(moon_average)) / (w * h);
blurred_moon = blurred_moon - moon_average;

% normalize the blurred_moon within [0, 255]
blurred_moon = (blurred_moon - min(min(blurred_moon))) / (max(max(blurred_moon)) - min(min(blurred_moon))) * 255;
blurred_moon = uint8(round(blurred_moon));






figure(1);
imshow(blurred_moon);