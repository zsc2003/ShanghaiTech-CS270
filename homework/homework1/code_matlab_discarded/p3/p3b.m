clear;clc;

origin_lena = imread('../../origin_images/lena_noisy.tif');
[w, h] = size(origin_lena);


% Gaussian filter


for i=1:2:31
    gaussian_filter = fspecial('gaussian', i, 1);
    gaussian_lena = imfilter(origin_lena, gaussian_filter, 'replicate');

    figure(1);
    imshow(gaussian_lena);
    title('hsize = ' + string(i)');
    pause(0.5);



    figure(range);
    imshow(median_lena);
    title('Gaussian filtered lena with kernel size ' + string(kernel_size));
    pause(0.5) % the pause is added to make sure the title is on the correspondence image
end