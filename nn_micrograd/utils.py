from graphviz import Digraph 
import os
import math
import random

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
        dot.node(name = uid, label = "{ %s | data %.4f | grad %.4f }" % (n.label, n.data, n.grad), shape = 'recod')
        if n._op:
            #se il valore è il risultato di qualche operazione crea il nodo per l'operaizone
            dot.node(name = uid + n._op, label = n._op)
            dot.edge(uid + n._op, uid)
    for n1,n2 in edges:
        dot.edge(str(id(n1)), str(id(n2)) + n2._op)
    return dot


def lol(): #gradient check (aggiungi h dove vuoi calcolare la derivata)

    h = 0.0001
    a = Value(2.0, label = 'a')
    b = Value(-3.0, label = 'b')
    c = Value(10.0, label = 'c')
    e = a*b; e.label = 'e'
    d = e + c; d.label = 'd'
    f = Value(-2.0, label = 'f')
    L = d * f; label = 'L'
    L1 = L.data

    a = Value(2.0 + h, label = 'a')
    b = Value(-3.0, label = 'b')
    c = Value(10.0, label = 'c')
    e = a*b; e.label = 'e'
    d = e + c; d.label = 'd'
    f = Value(-2.0, label = 'f')
    L = d * f; label = 'L'
    L2 = L.data + h

    print((L2 - L1)/h)





class Value:
    def __init__(self, data, _children = (), _op = '', label = ''):
        self.data = data
        self._prev = set(_children) #è il set dei figli
        self._op = _op
        self._backward = lambda: None #di default non fa nulla
        self.label = label
        self.grad = 0
        


    def __repr__(self):
        return f"Value(data = {self.data})"
    

    #python non sa come sammare due value object , quindi devo creare una funzione per sommarli 

    def __add__(self, other):
        other = other if isinstance(other,Value) else Value(other)
        out = Value(self.data + other.data, (self, other), '+')

        def _backward():
            self.grad += 1.0 * out.grad
            other.grad += 1.0 * out.grad
        out._backward = _backward

        return out #return a new value
    

    def exp(self):
        x = self.data
        out = Value(math.exp(x), (self, ), 'exp')

        def _backward():
            self.grad += out.data * out.grad
        out._backward = _backward
        return out
    

    def __pow__(self, other):
        assert isinstance(other, (int, float)), "jsajh"
        out = Value(self.data**other, (self,), f'**{other}')

        def _backward():
            self.grad += other * (self.data ** (other-1)) * out.grad
        out._backward = _backward
        return out


    def __mul__(self, other):
        other = other if isinstance(other,Value) else Value(other)
        out = Value(self.data * other.data, (self, other), '*')

        def _backward():
            self.grad = other.data * out.grad
            other.grad = self.data * out.grad
        out._backward = _backward

        return out #return a new value

    def __rmul__(self, other):
        return self * other
    

    def __truediv__(self, other):
        return self * other**-1
    

    def __neg__(self):
        return self * -1
    

    def __sub__(self, other):
        return self + (- other)
        



    def tanh(self):
        n = self.data
        t = (math.exp(2*n) - 1) / (math.exp(2*n) + 1)
        out = Value(t, (self, ), 'tanh')

        def _backward():
            self.grad = (1- t**2) * out.grad
        out._backward = _backward
        return out
     
    
    def backward(self):
        topo = []
        visited = set()
        def build_topo(v):
            if v not in visited:
                visited.add(v)
                for child in v._prev:
                    build_topo(child)
                topo.append(v)
        build_topo(self) #topological order of self

        self.grad = 1.0
        for node in reversed(topo):
            node._backward()


