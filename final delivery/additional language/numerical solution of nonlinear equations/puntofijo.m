% fixed point method.

%input:
% f, continuous function
% g, continuous function
% x0, initial guess
% tol, tolerance
% Nmax, maximum number of iterations

% output
% x, solution
% iter, number of iterations
% err, error

function [x,iter,err]=puntofijo(g,x0,tol,Nmax)

xant=x0;
E=1000; 
cont=0;

while E>tol && cont<Nmax
  xact=g(xant);
  E=abs(xact-xant);
  cont=cont+1;
  xant=xact;
end

x=xact;
iter=cont;
err=E;
end