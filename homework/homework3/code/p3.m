% In this problem, you need to turn sea_house.jpg to super pixel style using SLIC algorithm with cluster center 100, 500 and 1000
% (In practice, number of cluster center can be different with these values, but should be close to these values) show the result images.
% Show the result and tell the tile angle in your report.
clear;
close;

image = imread('images/sea_house.jpg');
image = im2double(image);

num_clusters = [100, 500, 1000];
results = cell(1, length(num_clusters));
for i = 1:length(num_clusters)
    results{i} = super_pixel(image, num_clusters(i), 30);
end

imwrite(image, "figures/sea-house-original.png");
imwrite(results{1}, "figures/sea-house-100.png");
imwrite(results{2}, "figures/sea-house-500.png");
imwrite(results{3}, "figures/sea-house-1000.png");

% Super pixel with Simple Linear Iterative Clustering (SLIC)
% Input:
%   image: input image
%   num_clusters: number of superpixels
%   num_iterations: number of iterations
% Output:
%   result: superpixel
function result = super_pixel(image, num_clusters, num_iterations)
    % Initialize cluster centers
    [height, width, ~] = size(image);

    % Convert image to feature space
    lab_image = rgb2lab(image);
    pos_image = cat(3, ...
        repmat(1:height, [width, 1])', ...
        repmat(1:width, [height, 1]) ...
    );

    % Initialize center
    step = round(sqrt(height * width / num_clusters));
    [cx, cy] = meshgrid( ...
        round(step / 2):step:width - 1, ...
        round(step / 2):step:height - 1 ...
    );
    centers = [cy(:), cx(:)];
    move_centers(centers, image);
    size(centers)

    lab_center = zeros(size(centers, 1), size(lab_image, 3));
    pos_center = zeros(size(centers, 1), size(pos_image, 3));
    
    for k = 1:size(lab_image, 3)
        lab_slice = lab_image(:, :, k);
        lab_center(:, k) = lab_slice(sub2ind(size(lab_slice), centers(:, 1), centers(:, 2)));
    end
    for k = 1:size(pos_image, 3)
        pos_slice = pos_image(:, :, k);
        pos_center(:, k) = pos_slice(sub2ind(size(pos_slice), centers(:, 1), centers(:, 2)));
    end

    % Initialize label and distance
    label = zeros(height, width);
    distance = Inf(height, width);

    % K-means clustering
    for iter = 1:num_iterations
        for i = 1:size(centers, 1)
            % 2 * step region around the center
            ymin = max(1, pos_center(i, 1) - step);
            ymax = min(height, pos_center(i, 1) + step);
            xmin = max(1, pos_center(i, 2) - step);
            xmax = min(width, pos_center(i, 2) + step);

            % Extract the region of interest from the feature matrix
            lab_feature = reshape(lab_image(ymin:ymax, xmin:xmax, :), [], 3);
            pos_feature = reshape(pos_image(ymin:ymax, xmin:xmax, :), [], 2);

            % Calculate the Euclidean distance
            lab_distance = sqrt(sum((lab_feature - lab_center(i, :)) .^ 2, 2));
            pos_distance = sqrt(sum((pos_feature - pos_center(i, :)) .^ 2, 2)) / step * 20;
            local_distance = sqrt(lab_distance .^ 2 + pos_distance .^ 2);
            local_distance = reshape(local_distance, ymax - ymin + 1, xmax - xmin + 1);

            % Update label and distance matrices
            mask = local_distance < distance(ymin:ymax, xmin:xmax);

            old_labels = label(ymin:ymax, xmin:xmax);
            old_labels(mask) = i;
            label(ymin:ymax, xmin:xmax) = old_labels;

            old_distance = distance(ymin:ymax, xmin:xmax);
            old_distance(mask) = local_distance(mask);
            distance(ymin:ymax, xmin:xmax) = old_distance;
        end

        % Update cluster centers
        for i = 1:size(centers, 1)
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
    center_colors = zeros(size(centers, 1), 3);
    for i = 1:size(centers, 1)
        center_colors(i, :) = image(pos_center(i, 1), pos_center(i, 2), :);
    end

    % Assign the color of each center to each pixel
    % Using label as index
    % label = enforce_connectivity(label, centers);
    % label
    label = reshape(label, [], 1);
    result = zeros(height, width, 3);
    for c = 1:3
        result(:, :, c) = reshape(center_colors(label, c), height, width);
    end
end

% Move center to local gradient minimum
% Input:
%   centers: cluster centers
%   image: input image
% Output:
%   centers: cluster centers
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
