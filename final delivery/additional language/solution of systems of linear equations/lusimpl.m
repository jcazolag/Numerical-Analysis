% LU factorization method with simple Gaussian elimination.

%input:
% A, invertible matrix
% b, constant vector

% output
% x, solution
% L, factorization matrix L
% U, matrix U of the factoring

function [x,L,U]=lusimpl(A,b)

n=size(A,1);
L=eye(n);
U=zeros(n);
M=A;

for i=1:n-1
    for j=i+1:n
        if M(j,i)~=0
           L(j,i)=M(j,i)/M(i,i);
           M(j,i:n)=M(j,i:n)-(M(j,i)/M(i,i))*M(i,i:n);           
        end
    end
    U(i,i:n)=M(i,i:n);
    U(i+1,i+1:n)=M(i+1,i+1:n);
end
U(n,n)=M(n,n);

z=sustprgr([L b]);
x=sustregr([U z]);
end

