#!/usr/bin/env python 2.7
import time
import pylab as pl #grafica
#complejidad lineal
def fib(n): # Regresa numero n de Fibonacci
        #result = []
        a, b = 0, 1
        for i in range(n):
            #result.append(a) # opcionalmente se puede regresar result con la sucesion de Fibonacci
            a, b = b, a+b
        return a        
X,Y,Z=[],[],[]

for i in range(35):
        X.append(i)  
        t = time.time()    
        Z.append(fib(i))        
        Y.append(time.time() - t)
        
print(Z) #sucession de Fibonacci
pl.xlabel('Numero de Fibonacci')
pl.ylabel('Tiempo de ejecucion') 
pl.title('Fibonacci iterativo')
pl.plot(X,Y,'r') # n(Dominio) contra tiempo(Rango)
pl.legend(( 'Complejidad', ) ) 
pl.savefig("Fiboi.png")  # produce a .png file  
pl.show()             
