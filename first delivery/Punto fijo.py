import sympy as sp
import numpy as np
import pandas as pd
x=sp.symbols('x')

def funcion(ecua='x+2'):
    global x
    return sp.sympify(ecua)
""" ecuacion tipo: string
    x_0: valor inicial tipo:float
    e_s tolerancia estimada tipo:float"""
def MetodoPF(ecuacion,x_0,es):
    global x
    ecuacion=funcion(ecuacion)+x #tal q sea g(x)
    ea=100
    x_r=x_0 #x_i+1
    iteracion=0 #inicio del contador en 0
    while ea>es:
        x_anterior=x_r# x_anterior = x_i
        x_r=ecuacion.evalf(subs={x:x_anterior})#xr=g(x_anterior)
        iteracion+=1#contador incrementado en 1
        if x_r !=0:
            ea=abs((x_r-x_anterior)/x_r)*100
    return x_r
#iniamos el programa con lo siguiente parametros
a=MetodoPF('exp(-x)-x',0,0.01)
print(a)