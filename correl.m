
function [result]= correl(m0, m1, m2)
    [x,y,~] = size(m2);
    result(1:x-2,1:y-2,3) = int8(0);
    for j=1:x-2
        for k=1:y-2
            submatriz=[
                m2(j  ,k,1), m2(j  ,k+1,1), m2(j  ,k+2,1);
                m2(j+1,k,1), m2(j+1,k+1,1), m2(j+1,k+2,1);
                m2(j+2,k,1), m2(j+2,k+1,1), m2(j+2,k+2,1)
                ];
            result(j,k,1) = sqrt((sum(sum(m0 .* submatriz)))^2 + ...
                                 (sum(sum(m1 .* submatriz)))^2);
        end
    end
    result(:,:,2)=result(:,:,1);
    result(:,:,3)=result(:,:,1);
    result(result>255) = 255;
end