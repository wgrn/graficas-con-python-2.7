#! encoding: utf-8
#!/usr/bin/env python 2.7
from numpy import * #es para random
import time
import pylab as pl #grafica
# complejidad de Dijkstra: 

inf = 1000000 # infinity

'''
def creaGrafo():
        print '\tDijkstra\n\n Creacion del grafo:\n\n'
        
        

        a = raw_input('Introduce peso de la arista--> ')
        d = raw_input('La arista tiene direccion? (s/N) N por defecto--> ')
        v1= raw_input('Introduce vertice 1--> ')
        v2= raw_input('Introduce vertice 2--> ')
        v2= raw_input('Finalizar--> ')
'''        
        

class Vertex():
        def __init__(self, v):
                self.vertex = v                  
        
class Edge(): # direction: True or False
        def __init__(self, a, d, v1, v2):
                self.weight = a
                self.d = d
                self.v1 = Vertex(v1)
                self.v2 = Vertex(v2)                        
                      
class Graph:
        def __init__(self, E):
                self.V, self.E = [], E
                for e in E:
                        self.V.append(e.v1.vertex)
                        self.V.append(e.v2.vertex) 
                self.V = list(set(self.V))
                '''
                for i in range(len(self.V)): 
                        aux = []
                        aux.append(self.V[i])
                        for e in E:
                                if (self.V[i]==e.v1.vertex):
                                        aux.append(e.v2.vertex)
                                if e.d and (self.V[i]==e.v2.vertex):
                                        aux.append(e.v1.vertex)
                        #aux = list(set(aux))
                        self.V[i] = aux
                                         '''            

class Node():
        def __init__(self, v, dv):
                self.vertex, self.dv, self.Pv = v, dv, None
                
def Decrease(Q, v, dv):
        for i in Q:
                if i.vertex==v:
                        i.dv = dv              
        return sorted(Q, key=lambda llave: llave.dv)    
            
def w(uE, u, E):# edge weight
        for i in E:
                if not i.d and ((i.v1.vertex==uE and i.v2.vertex==u) or (i.v1.vertex==u and i.v2.vertex==uE)):
                        return i.weight
                elif i.d and (i.v1.vertex==uE and i.v2.vertex==u):
                        return i.weight
        return inf                       
        
def Dijkstra(G, s):
        Q = []
        for v in G.V:
                dv = inf              
                Q.append(Node(v[0], dv))
        ds = 0
        Q = Decrease(Q, s, ds)
        Vt = [] 
        for i in range(len(G.V)):
                uE, Q = Q[0], Q[1:]
                Vt.append(uE) # tree vertices
                for u in Q: # u adyacente a uE
                        dw = uE.dv + w(uE.vertex, u.vertex, G.E)
                        if dw < u.dv:
                                u.dv, u.Pv = dw, uE
                                Q = Decrease(Q, u.vertex, u.dv)
        return Vt   
        
def imprime(tree, vertex):
        if vertex.Pv==None:
                print vertex.vertex,
                return
        else:
                imprime(tree, vertex.Pv)
                print '-',vertex.vertex,                    
'''
E = [] # figure 9.11
        # Grafo no dirijido
edge = Edge(3, False, 'a', 'b') # cost, direction, vertex1, vertex2
E.append(edge)
edge = Edge(7, False, 'a', 'd')
E.append(edge)
edge = Edge(4, False, 'b', 'c')
E.append(edge)
edge = Edge(2, False, 'b', 'd')
E.append(edge)                 
edge = Edge(5, False, 'd', 'c')
E.append(edge)
edge = Edge(6, False, 'c', 'e')
E.append(edge)
edge = Edge(4, False, 'd', 'e')
E.append(edge)
'''

'''
E = [] # exercise 2.a
        # Grafo dirijido
edge = Edge(3, True, 'b', 'a') # cost, direction, vertex1, vertex2
E.append(edge)
edge = Edge(7, True, 'a', 'd')
E.append(edge)
edge = Edge(4, True, 'b', 'c')
E.append(edge)
edge = Edge(2, True, 'd', 'b')
E.append(edge)                 
edge = Edge(5, True, 'd', 'c')
E.append(edge)
edge = Edge(6, True, 'c', 'e')
E.append(edge)
edge = Edge(4, True, 'e', 'd')
E.append(edge)
'''

'''
E = [] # examen redes
        # Grafo no dirijido
edge = Edge(1, False, '1', '2') # cost, direction, vertex1, vertex2
E.append(edge)
edge = Edge(2, False, '1', '3')
E.append(edge)
edge = Edge(4, False, '1', '4')
E.append(edge)
edge = Edge(1, False, '3', '4')
E.append(edge)                 
edge = Edge(1, False, '4', '5')
E.append(edge)
edge = Edge(4, False, '2', '5')
E.append(edge)
edge = Edge(4, False, '2', '6')
E.append(edge)
edge = Edge(1, False, '5', '6')
E.append(edge)
        
Grafo = Graph(E)

print '\nvertex set V:\n\t',
for v in Grafo.V:
        print v,
        
print '\n\nedge set E (vertex1, weight, vertex2):'      
for e in Grafo.E:
        if e.d:
                print '\t|',e.v1.vertex,'|--', e.weight,'->|', e.v2.vertex,'|'
        else:
                print '\t|',e.v1.vertex,'|--', e.weight,'--|', e.v2.vertex,'|'
        print '\t-----\t    -----'
print

tree = Dijkstra(Grafo, '6') # Graph, source vertex
for v in tree:
        imprime(tree, v)
        if v.dv != inf:
                print '\tlength:',v.dv
        else:
                print '\tlength: infinity'        

print '______________________________________\n\n'  

'''      
X,Y,E =[],[],[] # Grafica
for i in range(2, 100):        
        c1 = chr(random.randint(1,i))
        c2 = chr(random.randint(1,i))
        if c1!=c2:   
                r = random.randint(1,20)  
        else:
                r = 0           
        edge = Edge(r, False, c1, c2)
        E.append(edge) 
          
        Grafo = Graph(E)
        X.append(len(Grafo.V)) # Dominio
        
        t = time.time()
        tree = Dijkstra(Grafo, Grafo.V[random.randint(0,len(Grafo.V))])
        Y.append(time.time() - t) # Rango
        
        c1 = Grafo.V[random.randint(0,len(Grafo.V))]
        c2 = Grafo.V[random.randint(0,len(Grafo.V))]
        if c1!=c2:   
                r = random.randint(1,20)  
        else:
                r = 0           
        edge = Edge(r, False, c1, c2)
        E.append(edge)         

for v in tree:
        imprime(tree, v)
        print '\tlength:',v.dv         
        
pl.xlabel('cantidad de vertices')
pl.ylabel('Tiempo de ejecucion') 
pl.title('Dijkstra')
pl.plot(X,Y,'r') # n(Dominio) contra tiempo(Rango)
pl.legend(( 'Dijkstra', ) ) 
pl.savefig("Dijkstra.png")  # produce a .png file  
pl.show()  

