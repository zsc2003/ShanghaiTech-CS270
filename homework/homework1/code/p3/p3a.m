origin_lena = imread('../../origin_images/lena_noisy.tif');
[w, h] = size(origin_lena);

% median filter
for range = 1:3
    median_lena = uint8(zeros(w, h));
    kernel_size = 2 * range + 1;
    
    for i = 1:w
        for j = 1:h

            neighbouring_pixels = [];
            for x = -range:range
                for y = -range:range
                    if i + x > 0 && i + x <= w && j + y > 0 && j + y <= h
                        neighbouring_pixels = [neighbouring_pixels, origin_lena(i + x, j + y)];
                    end
                end
            end

            median_lena(i, j) = median(neighbouring_pixels);

        end
    end
    
    figure(range);
    imshow(median_lena);
    title('median filtered lena with kernel size ' + string(kernel_size));
    pause(0.5) % the pause is added to make sure the title is on the correspondence image
end