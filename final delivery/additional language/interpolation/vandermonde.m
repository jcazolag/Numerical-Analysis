% Vandermonde method

%input:
% X, abscissa
% Y, ordered

% output
% Coef, coefficients of the polynomial

function Coef=vandermonde(X,Y)

n=length(X);
A=zeros(n);

for i=1:n
    A(:,i)=(X.^(n-i))';
end

Coef=A\Y';

end