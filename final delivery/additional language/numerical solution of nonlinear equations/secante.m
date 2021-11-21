% secant method

%input:
% f, continuous function
% x0, initial guess
% x1, initial guess
% tol, tolerance
% Nmax, maximum number of iterations

% output
% x, solution
% iter, number of iterations
% err, error

function [x,iter,err]=secante(f,x0,x1,tol,Nmax)

f0=f(x0);
f1=f(x1);
E=1000; 
cont=1;

while E>tol && cont<Nmax
  xact=x1-f1*(x1-x0)/(f1-f0);
  fact=f(xact);
  E=abs(xact-x1);
  cont=cont+1; 
  x0=x1;
  f0=f1;
  x1=xact;
  f1=fact;
end

x=xact;
iter=cont;
err=E;
end 