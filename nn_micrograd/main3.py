import math 
import numpy as np 
import matplotlib.pyplot as plt
import torch

from utils import Value, draw_dot, lol
from classe import Layer, Neuron, MLP

#input
x1 = torch.Tensor( [2.0] ).double();    x1.requires_grad = True #con double da float32 diventa float64    
x2 = torch.Tensor( [0.0] ).double();    x2.requires_grad = True
#weights
w1 = torch.Tensor( [-3.0] ).double();   w1.requires_grad = True
w2 = torch.Tensor( [1.0] ).double();    w2.requires_grad = True
#bias
b = torch.Tensor( [6.8813735870195432] ).double(); b.requires_grad = True
n = x1*w1 + x2*w2 + b
o = torch.tanh(n)
print('----------------------------------------')
print('forward pass\t',o.data.item())#item ritorna l'elemento del tensore
o.backward()

print('----------------------------------------')
print('x2\t', x2.grad.item())#x2.grad è un tensore
print('w2\t', w2.grad.item())
print('x1\t', x1.grad.item())
print('w1\t', w1.grad.item())


print('----------------------------------------')

x = [2.0, 3.0, -1.0]
n = MLP(3, [4, 4, 1])
print(n(x))
draw_dot(n(x)).render('output_nn', view=False)

print('----------------------------------------')
xs = [
    [2.0, 3.0, -1.0],
    [3.0, -1.0, 0.5],
    [0.5, 1.0, 1.0],
    [1.0, 1.0, -1.0]
]
#ys = [Value(1.0), Value(-1.0), Value(-1.0), Value(1.0)] #target
ys = [1.0, -1.0, -1.0, 1.0] #target





for k in range(100):

    #forward pass
    ypred = [n(x) for x in xs] 

    #evaluate loss
    loss = Value(0.0) #compute loss
    for ygt, yout in zip(ys, ypred):
        loss += (yout - ygt) ** 2
    
    #prima del backword pass devi azzerare i gradienti 
    for p in n.parameters():
        p.grad = 0.0
    #backward pass
    loss.backward() 

    #update parametrs
    for p in n.parameters():
        p.data += -0.05 * p.grad

    print(f'k -> {k};\t\tlosss -> {loss.data}')

print(ypred, ys)





















