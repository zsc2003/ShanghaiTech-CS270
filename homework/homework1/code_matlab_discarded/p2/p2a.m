clear;clc;

origin_moon = imread('../../origin_images/moon.jpg');
% origin_moon = imread('../../origin_images/test.png');
% take the first channel of the image
% origin_moon = origin_moon(:, :, 1);
% normalize the image
%origin_moon = uint8(round(double(origin_moon) * 255.0));
figure(3);
imshow(origin_moon);


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
% shape to 3*3
I_xx = reshape([[0,1,0],[0, -2, 0],[0,1,0]], 3, 3);
I_yy = reshape([[0,0,0],[1, -2, 1],[0,0,0]], 3, 3);
Laplace = reshape([[0,1,0],[1,-4,1],[0,1,0]], 3, 3);

image_x = conv2(origin_moon, I_xx);
image_y = conv2(origin_moon, I_yy);
full = conv2(origin_moon, Laplace);

% ignore the zero padding
image_x = image_x(2:w+1, 2:h+1);
image_y = image_y(2:w+1, 2:h+1);
full = full(2:w+1, 2:h+1);

% normalize the image to [0, 255]
maxn = max(max(image_x));
minn = min(min(image_x));
image_x = uint8(round(double(image_x - minn) / (maxn - minn) * 255.0));

maxn = max(max(image_y));
minn = min(min(image_y));
image_y = uint8(round(double(image_y - minn) / (maxn - minn) * 255.0));

maxn = max(max(full));
minn = min(min(full));
full = uint8(round(double(full - minn) / (maxn - minn) * 255.0));

figure(1);
imshow(image_x);

figure(2);
imshow(image_y);

figure(4);
imshow(full);