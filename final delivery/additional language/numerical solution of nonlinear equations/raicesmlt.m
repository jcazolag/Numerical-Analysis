% multiple roots method

%input:
% f, continuous function
% f ', continuous function
% f '', continuous function
% x0, initial guess
% tol, tolerance
% Nmax, maximum number of iterations

% output
% x, solution
% iter, number of iterations
% err, error

function [x,iter,err]=raicesmlt(f,df,d2f,x0,tol,Nmax)

xant=x0;
fant=f(xant);
E=1000; 
cont=0;

while E>tol && cont<Nmax
  xact=xant-fant*df(xant)/((df(xant))^2-fant*d2f(xant));
  fact=f(xact);
  E=abs(xact-xant);
  cont=cont+1;
  xant=xact;
  fant=fact;
end

x=xact;
iter=cont;
err=E;
end 