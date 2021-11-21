% bisection method.

%input:
% f, continuous function
% a, right end of initial interval
% b, end end of end range
% tol, tolerance
% Niter, maximum number of iterations

% output
% x, solution
% iter, number of iterations
% err, error

function [x,iter,err]=biseccion(f,a,b,tol,Niter)

fa=f(a);
pm=(a+b)/2;
fpm=f(pm);
E=1000; 
cont=1;

while E>tol && cont<Niter
  if fa*fpm<0
     b=pm; 
  else
     a=pm;    
  end
  p0=pm;
  pm=(a+b)/2;
  fpm=f(pm);
  E=abs(pm-p0);
  cont=cont+1;
end

x=pm;
iter=cont;
err=E;
end