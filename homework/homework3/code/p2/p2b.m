clear; clc;

image = imread('../../images/origin_images/nebula.jpg');
intensity = double(rgb2gray(image));

% resize to the power of 2
[w, h] = size(intensity);
new_w = 2 ^ nextpow2(w);
new_h = 2 ^ nextpow2(h);

intensity = padarray(intensity, [new_w - w, new_h - h], 0, 'post');

a = 0.7;
b = 170;

for block_size = [4, 8]
    figure;
    subplot(1, 3, 1);
    imshow(image, []);
    title('origin image');

    splited_block = split(intensity, block_size, a, b, w, h);
    merged_block = merge(intensity, splited_block, a, b);
    merged_block = merged_block(1:w, 1:h);

    subplot(1, 3, 3);
    imshow(merged_block, []);
    title('foreground image');

    set(gcf, 'Units', 'Inches');
    pos = get(gcf, 'Position');
    set(gcf, 'PaperPositionMode', 'Auto', 'PaperUnits', 'Inches', 'PaperSize', [pos(3), pos(4)]);
    print(gcf, "../../images/p2/p2b_blocksize_" + num2str(block_size) + ".png", '-dpng', '-r300');
end

function mask = merge(intensity, S, a, b)
    mask = zeros(size(intensity));
    max_dim = full(max(S(:)));

    % merge the blocks
    for dim = 1:max_dim
        [vals, r, c] = qtgetblk(intensity, S, dim);
        numblocks = length(r);
        for i = 1:numblocks
            region = intensity(r(i):r(i)+dim-1, c(i):c(i)+dim-1);
            sigma = std2(region);
            m = mean2(region);
            if (sigma > 1) && (0 < m) && (m < b)
                mask(r(i):r(i)+dim-1, c(i):c(i)+dim-1) = 1;
            end
        end
    end
end


function S = split(intensity, block_size, a, b, w, h)
    S = qtdecomp(intensity, @split_test, block_size, a, b);

    % visualize the blocks
    blocks = repmat(uint8(0),size(S));
    for dim = [1024 512 256 128 64 32 16 8 4 2 1];
        numblocks = length(find(S==dim));
        if (numblocks > 0)
            values = repmat(uint8(1),[dim dim numblocks]);
            values(2:dim,2:dim,:) = 0;
            blocks = qtsetblk(blocks,S,dim,values);
        end
    end

    blocks(end,1:end) = 1;
    blocks(1:end,end) = 1;

    subplot(1, 3, 2);
    imshow(blocks(1:w, 1:h), []);
    title('split blocks');
end


function flag = split_test(block, block_size, a, b)
    % input: m-by-m blocks stacked into an m-by-m-by-k array, where k is the number of blocks
    % output: a logical k-element vector values are 1 if the corresponding block should be split, and 0 otherwise

    [block_w, block_h, block_num] = size(block);

    % an array with length k, all elements are logical 0
    flag = false(block_num, 1);

    if block_w < block_size
        return;
    end

    for i = 1:block_num
        sigma = std2(block(:, :, i));
        m = mean2(block(:, :, i));
        flag(i) = (sigma <= a) && (0 < m) && (m < b);
        flag(i) = ~flag(i);
    end
end