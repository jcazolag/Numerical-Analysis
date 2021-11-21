% false rule method

%input:
% f, continuous function
% a, right end of initial interval
% b, end end of end range
% tol, tolerance
% Nmax, maximum number of iterations

% output
% x, solution
% iter, number of iterations
% err, error


function [x,iter,err]=reglafalsa(f,a,b,tol,Nmax)

fa=f(a);
fb=f(b);
pm=(fb*a-fa*b)/(fb-fa);
fpm=f(pm);
E=1000; 
cont=1;

while E>tol && cont<Nmax
  if fa*fpm<0
     b=pm; 
  else
     a=pm;    
  end 
  p0=pm;
  pm=(f(b)*a-f(a)*b)/(f(b)-f(a));
  fpm=f(pm);
  E=abs(pm-p0);
  cont=cont+1;
end

x=pm;
iter=cont;
err=E;
end