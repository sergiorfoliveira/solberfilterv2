clear variables
dx = int8([
            -1, 0, 1;
            -2, 0, 2;
            -1, 0, 1
          ]);
dy = transpose(dx);
immatriz = imread("C:\Users\F9910101\Pictures\Mario.jpg");
tic
temp=converttograyscale(immatriz);
toc
clear immatriz
tic;
result=correl(dx,dy,temp);
toc;
clear temp;
image(result);