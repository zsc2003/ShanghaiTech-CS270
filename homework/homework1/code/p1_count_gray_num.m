% count the number of each pixel value
function gray_num = p1_count_gray_num(origin_grain)
    [w, h] = size(origin_grain);

    % count the number of each pixel value
    gray_num = zeros(1, 256);
    for i = 1:w
        for j = 1:h
            gray_num(origin_grain(i, j) + 1) = gray_num(origin_grain(i, j) + 1) + 1;
        end
    end
end