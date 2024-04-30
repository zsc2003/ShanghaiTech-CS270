% load image in 'blurred.tif'
I = imread('blurred.tif');

% do fft and fftshift
F = fft2(I);
F = fftshift(F);
F = 20 * log(1+abs(F));

% show F
figure, imshow(F,[]);
title('FFT of the image');

% do radon transform and get the motion blur angle and distance and show the result after radon transform
[R,xp] = radon(I,0:179);
figure, imshow(R,[],'Xdata',xp,'Ydata',1:size(R,1),'InitialMagnification','fit');
xlabel('\theta (degrees)');
ylabel('x''');
colormap(hot), colorbar

% get the motion blur angle and distance
[~,ind] = max(R(:));
[angle,distance] = ind2sub(size(R),ind);
angle = xp(angle);

% do inverse radon transform
I2 = iradon(R,angle);
figure, imshow(I2,[]);


% print the theta and distance
fprintf('The motion blur angle is %f degrees\n',angle);
fprintf('The motion blur distance is %f pixels\n',distance);
