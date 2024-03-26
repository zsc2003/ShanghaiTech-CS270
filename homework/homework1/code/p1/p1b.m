origin_grain = imread('../../origin_images/grain.tif');
gray_num = p1_count_gray_num(origin_grain);

[w, h] = size(origin_grain);

prefix_sum = cumsum(gray_num) / (w * h);
prefix_gray = uint8(round(prefix_sum * 255));

% histogram of grain.tif after applying histogram equalization
hist_eq_grain = uint8(zeros(w, h));
for i = 1:w
    for j = 1:h
        hist_eq_grain(i, j) = prefix_gray(origin_grain(i, j) + 1);
    end
end

% hist_eq_grain
figure(1);
imshow(hist_eq_grain);
title('histogram equalized image');

figure(2);
gray_num = p1_count_gray_num(hist_eq_grain);
bar(0:255, gray_num);
xlabel('gray level');
ylabel('number of pixels');
title('histogram of histogram equalized image');