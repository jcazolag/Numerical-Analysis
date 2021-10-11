from numpy import absolute

# Metodo de newton

# input: f(x), f´(x), x0, niter, tol

def fx(x):
    y = pow(x,2)-3
    return y
def f2x(x):
    y = 2*x
    return y

x0 = float(input("x0: "))
nite = int(input("numero de iteraciones: "))
tol = float(input("tolerancia: "))

cont = 0
error = tol+1
while(cont>nite and error>tol):
    xn = x0 - (fx(x0)/f2x(x0))
    error = abs(xn-x0)
    ++cont
    x0=xn
if(error<=tol):
    print(xn, "es una raiz con toleracia = ",tol)
else:
    print("el metodo no converge")