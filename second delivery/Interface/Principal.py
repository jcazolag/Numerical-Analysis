from tkinter import *

from Newton import *

import tkinter as tk

root = tk.Tk()


root.title("Metodos Numericos")
root.geometry('750x350')

def action():
    return x

def Mnewton():
    vNewton = tk.Toplevel(root)
    vNewton.title("Newton")
    texto = Label(vNewton,text="Newton",font=("Orbitron",10))
    texto.place(x=30, y=10)

    f1 = Label(vNewton,text="F: ")
    f1.place(x=20, y=50)
    funcion1 = tk.Entry(vNewton)
    funcion1.place(x=40, y=50)

    xi = Label(vNewton,text="X0: ")
    xi.place(x=20, y=100)
    xCero = tk.Entry(vNewton)
    xCero.place(x=40, y=100)

    Ni = Label(vNewton,text="NI: ")
    Ni.place(x=20, y=150)
    nIte = tk.Entry(vNewton)
    nIte.place(x=40, y=150)

    T = Label(vNewton,text="T: ")
    T.place(x=20, y=200)
    tolerancia = tk.Entry(vNewton)
    tolerancia.place(x=40, y=200)

    resultado = Label(vNewton,text="")
    resultado.place(x=40, y=300)
    Fun = str(funcion1.get())
    xinicial = float(xCero.get())
    nIteraciones = int(nIte.get())
    tole = float(tolerancia.get())

    val = MetodoPF(Fun,xinicial,tole,nIteraciones)

    #res = f1 +" "+ f2 +" "+ x0 +" "+ nite +" "+ tol
    resultado.configure(text = val)

    button = tk.Button(vNewton, text="Obtener raiz",command=Mnewton)
    button.place(x=50, y=250, width=100, height=30)






























#Primer Grupo de metodos/////////////////////////////////////////////////////

texto = Label(root,text="Soluciones Numericas de ENL",font=("Orbitron",10))
texto.place(x=30, y=10)

Binc = tk.Button(root, text="Busquedas Incrementales",command=action)
Binc.place(x=50, y=50)

Bisec = tk.Button(root, text="Biseccion",command=action)
Bisec.place(x=50, y=100)

Rfalsa = tk.Button(root, text="Regla Falsa",command=action)
Rfalsa.place(x=50, y=150)

Pfijo = tk.Button(root, text="Punto fijo",command=action)
Pfijo.place(x=50, y=200)

Newton = tk.Button(root, text="Newton",command=Mnewton)
Newton.place(x=50, y=250)

Sec = tk.Button(root, text="Secante",command=action)
Sec.place(x=50, y=300)

Rmul = tk.Button(root, text="Raices Multiples",command=action)
Rmul.place(x=50, y=350)



#Segundo Grupo de metodos/////////////////////////////////////////////////////

texto = Label(root,text="Solucion de Sistemas de EL",font=("Orbitron",10))
texto.place(x=300, y=10)

Gauss = tk.Button(root, text="Metodo De Gauss",command=action)
Gauss.place(x=320, y=50)

Lu = tk.Button(root, text="Factorizacion LU",command=action)
Lu.place(x=320, y=100)

Doolitle = tk.Button(root, text="Doolitle",command=action)
Doolitle.place(x=320, y=150)

Crount = tk.Button(root, text="Crount",command=action)
Crount.place(x=320, y=200)

Cholesky = tk.Button(root, text="Cholesky",command=action)
Cholesky.place(x=320, y=250)

Jacobi = tk.Button(root, text="Jacobi",command=action)
Jacobi.place(x=320, y=300)

Gseidel = tk.Button(root, text="Gauss - Seidel",command=action)
Gseidel.place(x=320, y=250)



#Tercer Grupo de metodos/////////////////////////////////////////////////////

texto = Label(root,text="Interpolacion",font=("Orbitron",10))
texto.place(x=550, y=10)

Vmonde = tk.Button(root, text="Vandermonde",command=action)
Vmonde.place(x=560, y=50)

Ddiv = tk.Button(root, text="Diferencias Divididas",command=action)
Ddiv.place(x=560, y=100)

Lagrange = tk.Button(root, text="Lagrange",command=action)
Lagrange.place(x=560, y=150)

Splines = tk.Button(root, text="Splines 1 - 2",command=action)
Splines.place(x=560, y=200)


root.mainloop()


