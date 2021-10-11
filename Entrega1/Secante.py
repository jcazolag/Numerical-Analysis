from numpy import absolute

# Metodo de la secante

# input: f(x), x0, x1 niter, tol

def fx(x):
    y = pow(x,2)-3
    return y

x0 = float(input("x0: "))
x1 = float(input("x1: "))
nite = int(input("numero de iteraciones: "))
tol = float(input("tolerancia: "))

cont = 0
error = tol+1
while(cont>nite and error>tol):
    xn = x1-fx(x1)*(x1-x0)/(fx(x1)-fx(x1))
    error = abs(xn-x0)
    x0=x1
    x1=xn
    ++cont
if(error<=tol):
    print(xn, "es una raiz con toleracia = ",tol)
else:
    print("el metodo no converge")