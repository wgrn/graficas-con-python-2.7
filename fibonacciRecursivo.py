graficas-con-python-2.7
=======================

#!/usr/bin/env python 2.7
import time
import pylab as pl
#complejidad exponencial
def fib(n): # Regresa numero n de Fibonacci
        if n==0:
                return 0
        elif n==1:
                return 1
        else: 
                return fib(n-1)+fib(n-2)                
X,Y,Z=[],[],[]

for i in range(35):
        X.append(i)  
        t = time.time()    
        Z.append(fib(i))        
        Y.append(time.time() - t)
        
print(Z) #sucession de Fibonacci 
pl.xlabel('Numero de Fibonacci')
pl.ylabel('Tiempo de ejecucion') 
pl.title('Fibonacci recursivo')
pl.plot(X,Y,'r') # n(Dominio) contra tiempo(Rango) 
pl.legend(( 'Complejidad', ) )
pl.savefig("Fibor.png")  # produce a .png file    
pl.show()            
