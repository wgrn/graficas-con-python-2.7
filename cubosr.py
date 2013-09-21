#!/usr/bin/env python 2.7
#programa que suma los cubos de los numeros del ciclo for y grafica su complejidad computacional
import time
import pylab as pl #grafica
#complejidad bicuadrada O(n⁴), resultado de: sum i³,i=2 to n
def S(n):
        if n==1:
                return 1        
        else: 
                return S(n-1)+ n*n*n                               
X,Y,Z=[],[],[]

for i in range(1,1000):
        X.append(i)  
        t = time.time()    
        Z.append(S(i))        
        Y.append(time.time() - t)
        
#print("Z=",Z) # S(n) para todas las n de 1 a 1000
pl.xlabel('Numero de cubos sumados')
pl.ylabel('Tiempo de ejecucion') 
pl.title('S(n) recursivo')
pl.plot(X,Y,'r') # n(Dominio) contra tiempo(Rango)
pl.legend(( 'Complejidad', ) ) 
pl.savefig("snr.png")  # produce a .png file    
pl.show() 
