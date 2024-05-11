clear; clc;

image = imread('../../images/origin_images/seahouse.jpg');
image = im2double(image);

cluster_nums = [100, 500, 1000];
results = [cell(1, length(cluster_nums))];
for i = 1:length(cluster_nums)
    results{i} = SLIC(image, cluster_nums(i));
end

figure;
subplot(2, 2, 1);
imshow(image);
title('Original Image');
subplot(2, 2, 2);
imshow(results{1});
title('100 cluster centers');
subplot(2, 2, 3);
imshow(results{2});
title('500 cluster centers');
subplot(2, 2, 4);
imshow(results{3});
title('1000 cluster centers');

set(gcf, 'Units', 'Inches');
pos = get(gcf, 'Position');
set(gcf, 'PaperPositionMode', 'Auto', 'PaperUnits', 'Inches', 'PaperSize', [pos(3), pos(4)]);
print(gcf, '../../images/p3/p3.png', '-dpng', '-r300');


% SLIC superpixel segmentation
function result = SLIC(image, cluster_num)
    [height, width, ~] = size(image);

    % Initialize
    step = round(sqrt(height * width / cluster_num));

    % initialize cluster centers by sampling pixels at regular grid step
    [cx, cy] = meshgrid(round(step / 2):step:width - 1, round(step / 2):step:height - 1);
    centers = [cy(:), cx(:)];
    center_num = size(centers, 1);

    % Convert image to feature space
    lab_image = rgb2lab(image);
    pos_image = cat(3, repmat(1:height, [width, 1])', repmat(1:width, [height, 1]));

    lab_center = zeros(center_num, size(lab_image, 3));
    pos_center = zeros(center_num, size(pos_image, 3));

    % sub2ind : get the index of the element in the matrix
    for k = 1:size(lab_image, 3)
        lab_slice = lab_image(:, :, k);
        lab_center(:, k) = lab_slice(sub2ind(size(lab_slice), centers(:, 1), centers(:, 2)));
    end
    for k = 1:size(pos_image, 3)
        pos_slice = pos_image(:, :, k);
        pos_center(:, k) = pos_slice(sub2ind(size(pos_slice), centers(:, 1), centers(:, 2)));
    end

    % move cluster centers to the lowest gradient position in a 3 * 3 neighborhood
    move_centers(centers, image);

    % setup label and distance
    label = zeros(height, width);
    distance = Inf(height, width);

    % Assignment
    num_iterations=30;
    for iter = 1:num_iterations
        for i = 1:center_num
            % 2 * step region around the center
            ymin = max(1, pos_center(i, 1) - step);
            ymax = min(height, pos_center(i, 1) + step);
            xmin = max(1, pos_center(i, 2) - step);
            xmax = min(width, pos_center(i, 2) + step);

            % Extract the region of interest from the feature matrix
            lab_feature = reshape(lab_image(ymin:ymax, xmin:xmax, :), [], 3);
            pos_feature = reshape(pos_image(ymin:ymax, xmin:xmax, :), [], 2);

            % compute the distance between the center and each pixel in the region
            lab_distance = sqrt(sum((lab_feature - lab_center(i, :)) .^ 2, 2));
            pos_distance = sqrt(sum((pos_feature - pos_center(i, :)) .^ 2, 2)) / step * 20;
            local_distance = sqrt(lab_distance .^ 2 + pos_distance .^ 2);
            local_distance = reshape(local_distance, ymax - ymin + 1, xmax - xmin + 1);

            % Update label and distance matrices if D < d(i)
            mask = local_distance < distance(ymin:ymax, xmin:xmax);

            old_labels = label(ymin:ymax, xmin:xmax);
            old_labels(mask) = i;
            label(ymin:ymax, xmin:xmax) = old_labels;

            old_distance = distance(ymin:ymax, xmin:xmax);
            old_distance(mask) = local_distance(mask);
            distance(ymin:ymax, xmin:xmax) = old_distance;
        end

        % Update cluster centers
        for i = 1:center_num
            [y, x] = find(label == i);
            if ~isempty(y)
                for k = 1:size(lab_image, 3)
                    lab_slice = lab_image(:, :, k);
                    lab_center(i, k) = mean(lab_slice(sub2ind(size(lab_slice), y, x)));
                end
                for k = 1:size(pos_image, 3)
                    pos_slice = pos_image(:, :, k);
                    pos_center(i, k) = mean(pos_slice(sub2ind(size(pos_slice), y, x)));
                end
            end
        end
        pos_center = round(pos_center);
    end

    % Retrieve the color of each center
    center_colors = zeros(center_num, 3);
    for i = 1:center_num
        center_colors(i, :) = image(pos_center(i, 1), pos_center(i, 2), :);
    end

    % Assign the color of each center to each pixel, use the label as index
    label = reshape(label, [], 1);
    result = zeros(height, width, 3);
    for c = 1:3
        result(:, :, c) = reshape(center_colors(label, c), height, width);
    end
end

% move the center to the lowest gradient position in a 3 * 3 neighborhood
function centers = move_centers(centers, image)
    gray_image = rgb2gray(image);
    centers_left = centers - [0, 1];
    centers_right = centers + [0, 1];
    centers_up = centers - [1, 0];
    centers_down = centers + [1, 0];
    gradient_x = gray_image(sub2ind(size(image), centers_right(:, 1), centers_right(:, 2))) + gray_image(sub2ind(size(image), centers_left(:, 1), centers_left(:, 2))) - 2 * gray_image(sub2ind(size(image), centers(:, 1), centers(:, 2)));
    gradient_y = gray_image(sub2ind(size(image), centers_down(:, 1), centers_down(:, 2))) + gray_image(sub2ind(size(image), centers_up(:, 1), centers_up(:, 2))) - 2 * gray_image(sub2ind(size(image), centers(:, 1), centers(:, 2)));
    centers(:, 1) = centers(:, 1) + (gradient_y > 0) - (gradient_y < 0);
    centers(:, 2) = centers(:, 2) + (gradient_x > 0) - (gradient_x < 0);
end