% incremental search method

%input:
% f, continuous function
% x0, starting point
% h, step
% niter, maximum number of iterations

% output
% a, left end of range
% b, right end of range
% iter, number of iterations

function [a,b,iter]=busquedas(f,x0,h,niter)

xant=x0; 
fant=f(xant);
xact=xant+h; 
fact=f(xact);

for i=1:iter
    if fant*fact<0
        break;
    end
    xant=xact;
    fant=fact;
    xact=xant+h;
    fact=f(xact);
end

a=xant;
b=xact;
iter=i;
end