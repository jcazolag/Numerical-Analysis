% simple Gaussian elimination method.

%input:
% A, invertible matrix
% b, constant vector

% output
% x, solution

function x=gausspl(A,b) 

n=size(A,1);
M=[A b];

for i=1:n-1
    for j=i+1:n
        if M(j,i)~=0
           M(j,i:n+1)=M(j,i:n+1)-(M(j,i)/M(i,i))*M(i,i:n+1);
        end
    end
end

x=sustregr(M);
end