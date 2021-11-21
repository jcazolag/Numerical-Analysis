% Gauss-Seidel method

%input:
% A, invertible matrix
% b, constant vector
% x0, initial guess
% tol, tolerance
% Nmax, maximum number of iterations

% output
% x, solution
% iter, number of iterations
% err, error

function [x,iter,err]=gseidel(A,b,x0,tol,Nmax)

D=diag(diag(A));
L=-tril(A)+D;
U=-triu(A)+D;
T=inv(D-L)*U; 
C=inv(D-L)*b;
xant=x0;
E=1000;
cont=0;

while E>tol && cont<Nmax       
    xact=T*xant+C;
    E=norm(xant-xact);
    xant=xact;
    cont=cont+1;
end

x=xact;
iter=cont;
err=E;
end