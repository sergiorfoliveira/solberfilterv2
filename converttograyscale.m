function [matriz_out]=converttograyscale(matriz_in)
    [x,y,~] = size(matriz_in);
    matriz_out(1:x,1:y,1:3) = int8(0);
     for j=1:x
         for k=1:y
             matriz_out(j,k,1:3)=round(mean(matriz_in(j,k,:)));
         end
     end
end
