import sympy as sp
import numpy as np
import pandas as pd
x=sp.symbols('x')

def funcion(ecua='x+2'):
    global x
    return sp.sympify(ecua)
a=funcion()
def FalsaPosiModi(func,xl,xu,es):
    #definimos la raiz aproximada en 0
    global x
    ecuacion=funcion(func)
    ea=100 #Fff
    iu=0 #ff
    il=0 #FFF
    xr=0 #FFF
    iteracion=0 #contador de iteraciones
    #evaluamos la funciones
    fl=ecuacion.evalf(subs={x:xl})
    fu=ecuacion.evalf(subs={x:xu})
    #contenedores de datos
    m_itera=np.array([]) #matriz q almacena valores de itera
    m_xl=np.array([])   #matriz q alamacena valores de xl
    m_xu=np.array([])   #matriz q alamcena valores de xu
    m_xr=np.array([])   #matriz q almacena valroes de xr
    m_ea=np.array([])   #matriz q alamcena valore s de ea
    #iniciamos el bucle
    while ea>es:
        xa=xr
        xr=xu-fu*(xl-xu)/(fl-fu)
        fr=ecuacion.evalf(subs={x:xr})
        iteracion+=1
        if xr!= 0:
            ea=abs((xr-xa)/xr)*100
        test=fl*fr
        #agregamos valores a las matrices vacias
        m_itera=np.append(m_itera,iteracion)
        m_xl=np.append(m_xl,xl)
        m_xu=np.append(m_xu,xu)
        m_xr=np.append(m_xr,xr)
        m_ea=np.append(m_ea,ea)  
        if test<0: fu="ecuacion.evalf(subs={x:xu})" if="" il="" iu="0" xu="xr">=2:
                fl=fl/2
        elif test>0:
            xl=xr
            fl=ecuacion.evalf(subs={x:xl})
            il=0
            iu+=1
            if iu>=2:
                fu=fu/2
        else:
            ea=0
    #representamos datos en pandas
    iteracion=pd.Series(m_itera,name="Iteracion")
    xl=pd.Series(m_xl,name="xl")
    xu=pd.Series(m_xu,name="xu")
    xr=pd.Series(m_xr,name="xr")
    ea=pd.Series(m_ea,name="ea%")
    tabla=pd.concat([iteracion,xl,xu,xr,ea],axis=1) #unimos en columnas
    return tabla
        
a=FalsaPosiModi('x**10-1',0,1.3,10)           
print(a) 