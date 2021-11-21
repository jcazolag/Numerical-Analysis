from math import fabs
from math import sqrt
from sys import exit


"""def inputMatrix():"""
	"""Ingreso de datos de la matriz"""

	"""n = int(input("Ingrese el orden de la matriz: "))
	print "Ingrese los elementos de la matriz A fila por fila con un espacio luego enter"
	A = [[0.0]*n for i in range(n)]
	aux = [[0.0]*n for i in range(n)]
	for i in range(n):
		temp = raw_input()
		A[i] = temp.split()
		for j in range(n):
			A[i][j] = float(A[i][j])
	if A == aux:
		exit('Matriz nula, vuelva a escribir la matriz')
	return A		
"""

def inputVector(M):
	"""Ingreso de datos del vector independiente"""

	n = len(M)
	print('Ingrese los elementos del vector b')
	b = [0]*n
	#for i in range(n):
	#	b[i] = float(input())

	temp = raw_input();
	b = temp.split()
	for i in range(n):
		b[i] = float(b[i])

	return b	
	
def printMatrixD(M):
	"""Imprime la matriz, version debugger."""

	for i in range(len(M)):
		# print '|',
		for j in range(len(M[i])):
			if(i == 0 and j == 0):
				print " ",
				for x in range(len(M[i])):
					print '{0:8}'.format(x),
				print
				print
			if(j == 0):
				print i,

			if(j == len(M)):
				print '|',
				print '{0:8.4f}'.format(M[i][j]),
			else:
				print '{0:8.4f}'.format(M[i][j]),	
		print '|'
	print

def printMatrix(M):
	"""Imprime la matriz de una forma legible."""

	for i in range(len(M)):
		print '|',
		for j in range(len(M[i])):
			if(j == len(M)):
				print '|',
				print '{0:8.4f}'.format(M[i][j]),
			else:
				print '{0:8.4f}'.format(M[i][j]),	
		print '|'
	print  

def norm1(A):
	"""Calcula la norma 1"""

	summation = 0
	for i in range(len(A)):
		summation += abs(A[i][0])

	for j in range(1, len(A)):
		temp = 0
		for i in range(len(A[i])):
			temp += abs(A[i][j])
		summation = temp if (temp > summation) else summation

	return summation 

def infinityNorm(A):
	"""Calcula la norma infinita"""

	summation = 0
	for j in range(len(A)):
		summation += abs(A[0][j])

	for i in range(1, len(A)):
		temp = 0
		for j in range(len(A[i])):
			temp += abs(A[i][j])
		summation = temp if (temp > summation) else summation
			
	return summation  

def symmetricMatrix(A):
	"""Calcula la matriz simetrica de A"""

	for i in range(len(A)):
		for j in range(i+1,len(A)):
			if A[i][j] != A[j][i]:
				return False
	return True 

def trans(M):
	"""Calcula la matriz transpuesta de M"""

	n = len(M)
	return [[ M[i][j] for i in range(n)] for j in range(n)]

def reverseSub(a):
	"""Se usa para resolver la matriz superior de gauss/gauss-Jordan"""

	n = len(a)
	x = [0]*n
	for j in range(n-1, -1, -1):
		x[j] = (a[j][n] - sum(a[j][k]*x[k] for k in range(j+1, n)))/float(a[j][j])
	return x	

def solMatrixSup(M, b):
	"""Resuelve la matriz superior con el metodo inverso"""	

	x = []
	for i in range(len(M)-1,-1,-1):
		x.append((1.0/(M[i][i]))*(b[i]-sum(M[i][len(M)-j-1]*x[j] for j in range(len(x)))))
	x.reverse()
	
	return x

def solMatrixInf(M, b):
	"""Resuelve la matriz inferior con el metodo inverso"""

	x = []
	for i in range(len(M)):
		x.append((1.0/(M[i][i]))*(b[i]-sum(M[i][j]*x[j] for j in range(len(x)))))
	return x
	
def augmentedMatrix(M, b):
	"""Retorna la matriz aumentada"""
	
	a = M
	for i in range(len(M)):
		a[i].append(b[i])

	return a	

def maxColum(M, c):
	"""Devuelve la fila del mayor valor debajo de la diagonal en la columna c"""

	r = c #fila
	maximum = M[c][c]
	for i in range(c+1,len(M)):
		if(fabs(maximum) < fabs(M[i][c])):
			maximum = M[i][c]
			r = i
	return r

def maxSubMatrix(M, c):
	"""Retorna el mayor elemento de la submatriz A[c]"""

	row = c
	colum = c
	n = len(M)
	maximum = M[c][c]
		
	for j in range(c, n):
		for k in range(c, n):
			maxTemp = M[k][j]
			if(fabs(maximum) < fabs(maxTemp)):
				maximum = maxTemp
				colum = j
				row = k

	return row, colum			

def exchangeRows(M, r1, r2):
	"""Intercambia las filas r1 y r2 de M"""

	M[r1], M[r2] = M[r2], M[r1]
	return M

def exchangeCols(M, c1, c2):
	"""Intercambia las columnas c1 y c2 de M"""

	for k in range(len(M)):
		M[k][c1] , M[k][c2] = M[k][c2], M[k][c1]
	return M

def pivot(a, P, Q, colum, piv=0):
	"""Se encarga del pivoteo en cualquier metodo."""

	if piv > 2 or piv < 0:
		exit('Valores invalidos para el parametro pivoteo, valores validos: 0, 1, 2.')
	n = len(a)
		
	temp = a[colum][colum]
	if(temp == 0.0 and piv == 0):
		row_maxColumn = maxColum(a, colum)
		a = pivotP(a, row_maxColumn, colum)
		P = exchangeRows(P, row_maxColumn, colum)
		print 'P(%d,%d)' % (row_maxColumn, colum)
		printMatrix(Pr(n, row_maxColumn, colum))
		
	elif piv == 1:
		row_maxColumn = maxColum(a, colum)
		if row_maxColumn != colum:
			a = pivotP(a, row_maxColumn, colum)
			P = exchangeRows(P, row_maxColumn, colum)
			print 'P(%d,%d)' % (row_maxColumn, colum)
			printMatrix(Pr(n, row_maxColumn, colum))
			
	elif piv == 2:
		row, c = maxSubMatrix(a, colum)	
		if (row != colum) or (c != colum) :
			a = pivotT(a, colum)
			P = exchangeCols(P, row, colum)
			Q = exchangeCols(Q, colum, c)
			print 'P(%d,%d):' % (colum, row)
			printMatrix(Pr(n, row, colum))
			print 'Q(%d,%d):' % (colum, c)
			printMatrix(Pr(n, c, colum))
	
	#retorna la matriz, la matriz de permutacion de filas y la de columnas.	
	return 	a, P, Q		

def pivotP(M, r1, r2):
	"""Permuta la fila r1 con la fila r2 de la matriz M"""

	return exchangeRows(M, r1, r2)

def pivotT(M, i):
	"""Busca el mayor elemento de la submatriz A[i] y permuta filas y columnas"""

	r, c = maxSubMatrix(M, i)
	M = pivotP(M, i, r)		

	return exchangeCols(M, c, i)

def Doolittle(A, piv=0):

	n = len(A)
	U = [[0.0]*n for j in range(n)]
	L = [[float(i == j) for j in range(n)] for i in range(n)]
	P = [[float(i == j) for j in range(n)] for i in range(n)]
	Q = [[float(i == j) for j in range(n)] for i in range(n)]

	#pivot
	if piv:
		for j in range(len(A)):
			A, P, Q = pivot(A, P, Q, j, piv)

	for k in range(n):
		for i in range(n):
			U[k][i] = A[k][i] - sum(L[k][p]*U[p][i] for p in range(k))
		for i in range(k, n):
			if U[k][k] == 0:
				exit('Debe usarse pivoteo parcial')
			L[i][k] = (A[i][k] - sum(L[i][p]*U[p][k] for p in range(k))) / float(U[k][k])	

	if piv == 2:
		return P, Q, L, U
	return P, L, U