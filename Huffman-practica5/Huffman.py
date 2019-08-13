#! encoding: utf-8
#!/usr/bin/env python 2.7
from numpy import * #es para random
import time, random, string
import pylab as pl #grafica
# complejidad de Huffman logarítmico
# complejidad de descifrado cuadrático
 
class Conjunto:
        def __init__(self, char, freq):
                self.char = char
                self.freq = freq
                self.left = None # verifica si no tiene hijos
        def __repr__(self):
                return repr((self.char, self.freq))

class Node():
        def __init__(self):
                self.left = None
                self.right = None
       
def Huffman(C):
        Q = []
        for c in C: # Q = C
                conjunto = Conjunto(c,C[c])
                Q.append(conjunto)

        Q = sorted(Q, key=lambda llave: llave.freq)
        n = len(Q)

        for i in range(1,n):
                z = Node()
                z.left = x = Q[0]
                z.right = y = Q[1]
                Q = Q[2:]
                z.freq = x.freq + y.freq
                Q.append(z)
                Q = sorted(Q, key=lambda llave: llave.freq)        
        return Q[0]
            
def Diccionario(data): #recibe cadena y regresa frecuencias
        n, C = len(data), {}        
        for i in range(n):
                x = data[i]
                C[x]=0
                
        for i in range(n):
                x = data[i]
                C[x]+=1        

        return C

def busca(nodo,x,cad): #encuentra char y obtiene su codificacion bin
        if nodo.left==None:
                if nodo.char==x:                
                        return cad
                else:       
                        return ''
        else:   
                cade = busca(nodo.left, x, cad + '0')
                na = busca(nodo.right, x, cad + '1')
                if cade != '': return cade
                else: return na     

def prefix(s1, s2):
        if not s1 or not s2: return ''
        for i, c in enumerate(s1):
                if c != s2[i]:
                        return s1[:i]
        return s1
'''                   
f = open("entrada")
data = f.read()
f.close()

#data = 'abcbabcwntghowhomwrm8t82t2854t254u8t295p9{9¿+0lp-0¿lp¿0lpm¿0l+mp+9}babccbabd'
print '\ncadena de entrada:\n',data
C = Diccionario(data)
      
print '\nDiccionario frecuencias:',C,len(C)
                       
root = Huffman(C)
print 'frecuencia root: ',root.freq

Bin = {}
print
for c in C:
        Bin[c] = busca(root,c,'')
        print c,':',Bin[c]
        
print '\nDiccionario Bin:',Bin

cifrado = ''
for i in data:
        cifrado += Bin[i]
                
print '\ncadena cifrada:',cifrado 

g = open("cifrado.bin",'wb')
g.write(cifrado)
g.close()

g = open("cifrado",'w')
g.write(cifrado)
g.close()

descifrado = ''

for i in range(len(data)):
        for c in C:
                b = len(Bin[c])                
                aux = prefix(Bin[c], cifrado)  
                x = len(aux) 
                if x==b:
                        cifrado = cifrado[x:]
                        descifrado += c
                        
print 'cadena descifrada:\n',descifrado,'\n'

h = open("descifrado",'w')
h.write(descifrado)
h.close()

'''
X,Y,Y1,Y2,data =[],[],[],[],''
for i in range(1, 400):
        X.append(i) # Dominio
        data += random.choice(string.letters)
        
        #tiempo de codificacion 
        t = time.time()    
        C = Diccionario(data)
        t2 = time.time()
        root = Huffman(C)
        Y2.append(time.time() - t2)
        
        Bin = {}
        for c in C:
                Bin[c] = busca(root,c,'')

        cifrado = ''
        for i in data:
                cifrado += Bin[i]      
        Y.append(time.time() - t)
        
        
        #tiempo de descifrado
        t = time.time()    
        descifrado = ''
        for i in range(len(data)):
                for c in C:
                        b = len(Bin[c])                
                        aux = prefix(Bin[c], cifrado)  
                        x = len(aux) 
                        if x==b:
                                cifrado = cifrado[x:]
                                descifrado += c       
        Y1.append(time.time() - t) 
        
pl.xlabel('longitud de cadena')
pl.ylabel('Tiempo de ejecucion') 
pl.title('Huffman')
pl.plot(X,Y,'r',X,Y1,'b',X,Y2,'g') # n(Dominio) contra tiempo(Rango)
pl.legend(( 'cifrado','descifrado', 'Huffman' ) ) 
pl.savefig("cifrado.png")  # produce a .png file  
pl.show()  
                           
