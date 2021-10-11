# busquedas incrementales

#input: f(x), delta, x0, nite
def fx(x):
    y = x-3
    return y
delta = float(input("delta: "))
x0 = float(input("x0: "))
nite = int(input("numero de iteraciones: "))

if(fx(x0) == 0):
    print(x0, " es raiz")
else:
    xn = x0+delta
    ite = 0
    while(nite>= ite and fx(x0)*fx(xn)>0):
        x0 = xn
        xn = x0+delta
        ++ite
    if(fx(xn) == 0):
       print(xn, " es raiz") 
    elif(fx(x0)*fx(xn)<0):
        print("hay almenos una raiz en el intervalo [",x0,",",xn,"]")
    else:
        print("no se encuentró una raiz")

