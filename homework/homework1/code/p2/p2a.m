origin_moon = imread('../../origin_images/moon.jpg');
[w, h] = size(origin_moon);

p = 5;
q = 20;
m = 10;
n = 15;

% generate random image
img_a = randi([0, 255], p, q);
img_b = randi([0, 255], m, n);

conv_a = conv2(img_a, img_b);
conv_b = p2_convolution(img_a, img_b);

% judge whether the two convolution results are the same
if isequal(conv_a, conv_b)
    disp('The two convolution results are the same.');
else
    disp('The two convolution results are not the same.');
end






% figure(1);
% imshow(origin_moon);