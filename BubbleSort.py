#!/usr/bin/env python 2.7
from numpy import * #es para random
import time
import pylab as pl #grafica
#complejidad cuadratica
def BubbleSort(A):
        for i in range(len(A)-2): # recorre a A len(A)-1 veces
                for j in range(len(A)-1): # busca desde A[0] hasta A[len(A)-1]
                        if A[j]>A[j+1]:
                                A[j],A[j+1]=A[j+1],A[j]
                                
        return A                                    
X,Y,A=[],[],[]

for i in range(1,400):
        A.append(random.randint(1, 1000))
        X.append(i)  
        t = time.time()    
        A=BubbleSort(A)        
        Y.append(time.time() - t)
        
print("A=",A) #conjunto ordenado  
pl.xlabel('Longitud de arreglo de enteros A')
pl.ylabel('Tiempo de ejecucion') 
pl.title('BubbleSort')
pl.plot(X,Y,'r') # n(Dominio) contra tiempo(Rango)
pl.legend(( 'Complejidad', ) ) 
pl.savefig("bubble.png")  # produce a .png file    
pl.show()      
