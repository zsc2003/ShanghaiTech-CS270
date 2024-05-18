% clear; clc;

% image = imread('../../images/origin_images/nebula.jpg');

% region_size = [[8,8], [4,4]]
% results = [cell(1, length(region_size))];
% for i = 1:length(region_size)
%     result{i} = zeros(size(image));
%     Region_Splitting_and_Merging(image, results{i}, 1, size(image, 1), 1, size(image, 2), region_size(i));
% end

% % set(gcf, 'Units', 'Inches');
% % pos = get(gcf, 'Position');
% % set(gcf, 'PaperPositionMode', 'Auto', 'PaperUnits', 'Inches', 'PaperSize', [pos(3), pos(4)]);
% % print(gcf, '../../images/p2/p2b.png', '-dpng', '-r300');


% % Region Splitting and Merging
% % let result to be 0 / 1 which represents the region satisfies the condition(Q) or not
% % region_size is the minimum size of the region
% function result = Region_Splitting_and_Merging(image, result, up, down, left, right, region_size)
%     [height, width, ~] = size(image);

%     % split and merge
%     if down - up < region_size(1) || right - left < region_size(2)
%         Q = get_Q(region);
%         result(up:down, left:right) = Q;
%         return;
%     end

%     % split
%     x_mid = floor((up + down) / 2);
%     y_mid = floor((left + right) / 2);

%     region1 = image(up:x_mid, left:y_mid, :);
%     region2 = image(up:x_mid, y_mid+1:right, :);
%     region3 = image(x_mid+1:down, left:y_mid, :);
%     region4 = image(x_mid+1:down, y_mid+1:right, :);
    
    

% end


% function get_Q(image)
%     [height, width, ~] = size(image);
%     % if sigma > a and 0 < m < b, Q = True, else Q = False
%     % m is the mean of the region, sigma is the standard deviation of the region
%     % a = 0.7, b = 170
%     a = 0.7;
%     b = 170;
%     m = mean(image(:));
%     sigma = std(image(:));
%     Q = sigma > a && 0 < m < b;
%     return Q;
% end




clear; clc;

image = imread('../../images/origin_images/nebula.jpg');
result = regionSplitMerge(image, 0.7, 170); % 这里的10和200为示例阈值
imshow(uint8(result)*255);


function segmented_image = regionSplitMerge(input_image, a, b)
    % 输入图像转换为灰度图像

    % 初始化
    image_size = size(input_image);
    segmented_image = zeros(image_size);

    % 递归区域分割函数
    function splitAndMerge(x, y, width, height)
        sub_image = input_image(x:x+width-1, y:y+height-1);
        sigma = std(x(:));
        m = mean(sub_image(:));

        % 检查分割条件
        if width > 8 || height > 8
            if sigma > a && m > 0 && m < b
                % 继续分割
                midx = floor(width/2);
                midy = floor(height/2);
                splitAndMerge(x, y, midx, midy);
                splitAndMerge(x + midx, y, width - midx, midy);
                splitAndMerge(x, y + midy, midx, height - midy);
                splitAndMerge(x + midx, y + midy, width - midx, height - midy);
            else
                % 不分割，标记为1
                segmented_image(x:x+width-1, y:y+height-1) = 1;
            end
        end
    end

    % 开始递归过程
    splitAndMerge(1, 1, image_size(1), image_size(2));

    % 输出分割结果
    % intensity = double(rgb2gray(image)) / 256;
lab = segmented_image > 0;
end