% convolution of two images
function conv = p2_convolution(img_a, img_b)
    [m, n] = size(img_a);
    [p, q] = size(img_b);
    % flip the kernel with for loop
    flipped_img_b = zeros(p, q);
    for i = 1:p
        for j = 1:q
            % flipped_img_b(i, j) = img_b(p - i + 1, q - j + 1);

            % TODO:
            % flip or not?
            


            flipped_img_b(i, j) = img_b(i,j);
        end
    end
    
    conv = zeros(m + p - 1, n + q - 1);
    for i = 1:m
        for j = 1:n
            for k = 1:p
                for l = 1:q
                    conv(i+k-1, j+l-1) = conv(i+k-1, j+l-1) + img_a(i, j) * flipped_img_b(k, l);
                end
            end
        end
    end
end