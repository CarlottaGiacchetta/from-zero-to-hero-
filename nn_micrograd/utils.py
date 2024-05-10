from graphviz import Digraph 
import os

def trace(root):
    #costruisci un set di tutti i nodi e gli archi del grafo
    nodes, edges = set(), set()
    def build(v):
        if v not in nodes:
            nodes.add(v)
            for child in v._prev:
                edges.add((child, v))
                build(child)
    build(root)
    return nodes, edges

def draw_dot(root):

    


    # Add the path to Graphviz bin to the PATH environment variable
    os.environ["PATH"] += os.pathsep + r'C:\Users\carlo\Downloads\windows_10_cmake_Release_Graphviz-11.0.0-win64\Graphviz-11.0.0-win64\bin'
    dot = Digraph(format = 'png', graph_attr = {'rankdir' : 'LR'}, engine='dot') #LR = Left to Right
    nodes, edges = trace(root)
    for n in nodes:
        uid = str(id(n))
        #per ogni valore del grafo crea un rettangolo
        dot.node(name = uid, label = "{data %.4f}" % (n.data, ), shape = 'recod')
        if n._op:
            #se il valore è il risultato di qualche operazione crea il nodo per l'operaizone
            dot.node(name = uid + n._op, label = n._op)
            dot.edge(uid + n._op, uid)
    for n1,n2 in edges:
        dot.edge(str(id(n1)), str(id(n2)) + n2._op)
    return dot




class Value:
    def __init__(self, data, _children = (), _op = ''):
        self.data = data
        self._prev = set(_children) #è il set dei figli
        self._op = _op


    def __repr__(self):
        return f"Value(data = {self.data})"
    

    #python non sa come sammare due value object , quindi devo creare una funzione per sommarli 

    def __add__(self, other):
        out = Value(self.data + other.data, (self, other), '+')
        return out #return a new value

    def __mul__(self, other):
        out = Value(self.data * other.data, (self, other), '*')
        return out #return a new value
    






