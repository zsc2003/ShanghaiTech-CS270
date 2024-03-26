origin_tire = imread('../../origin_images/tire.tif');
[w, h] = size(origin_tire);

patch_size = 41;
patch_range = (patch_size - 1) / 2;
center_patch_size = 3;
center_range = (center_patch_size - 1) / 2;
step_size = 1;
rate = 0.02;
border_line = patch_size * patch_size * rate;

output_tire = uint8(zeros(w, h));

% CLAHE
for i = 1:step_size:w
    for j = 1:step_size:h
        % get the patch
        patch = uint8(zeros(patch_size, patch_size));
        for x = -patch_range:patch_range
            for y = -patch_range:patch_range
                x_idx = i + x;
                y_idx = j + y;
                
                % get the mirror pixel
                if x_idx <= 0
                    x_idx = w + x_idx;
                elseif x_idx > w
                    x_idx = x_idx - w;
                end
                if y_idx <= 0
                    y_idx = h + y_idx;
                elseif y_idx > h
                    y_idx = y_idx - h;
                end
                
                patch(x + patch_range + 1, y + patch_range + 1) = origin_tire(x_idx, y_idx);

            end
        end
        
        above_border = 0;
        gray_num = p1_count_gray_num(patch);

        for k = 1:256
            if gray_num(k) > border_line
                above_border = above_border + gray_num(k) - border_line;
                gray_num(k) = border_line;
            end
        end
        
        gray_num = gray_num + above_border / 256;
        prefix_sum = cumsum(gray_num) / (patch_size * patch_size);
        prefix_gray = uint8(round(prefix_sum * 255));

        for x = -center_range:center_range
            for y = -center_range:center_range
                x_idx = i + x;
                y_idx = j + y;
                
                % get the mirror pixel
                if x_idx <= 0
                    x_idx = w + x_idx;
                elseif x_idx > w
                    x_idx = x_idx - w;
                end
                if y_idx <= 0
                    y_idx = h + y_idx;
                elseif y_idx > h
                    y_idx = y_idx - h;
                end

                output_tire(x_idx, y_idx) = prefix_gray(origin_tire(x_idx, y_idx) + 1);
            end
        end

    end
end

% image after applying CLAHE
figure(1);
imshow(output_tire);
title('CLAHE processed image');

% histogram of applyed CIAHE image
figure(2);
gray_num = p1_count_gray_num(output_tire);
bar(0:255, gray_num);
xlabel('gray level');
ylabel('number of pixels');
title('histogram of CLAHE processed image');