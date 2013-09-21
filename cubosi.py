#!/usr/bin/env python 2.7
#programa que suma los cubos de los numeros del ciclo for y grafica su complejidad computacional
import time
import pylab as pl #grafica 
#complejidad lineal
def S(n):
        a=0
        for i in range(1,n+1):
                a+=i*i*i
        return a                               
X,Y,Z=[],[],[]

for i in range(1,1000):
        X.append(i)  
        t = time.time()    
        Z.append(S(i))        
        Y.append(time.time() - t)
        
#print("Z=",Z) # S(n) para todas las n de 1 a 1000 
pl.xlabel('Numero de cubos sumados')
pl.ylabel('Tiempo de ejecucion') 
pl.title('S(n) iterativo')
pl.plot(X,Y,'r') # n(Dominio) contra tiempo(Rango)
pl.legend(( 'Complejidad', ) ) 
pl.savefig("sni.png")  # produce a .png file    
pl.show()    
