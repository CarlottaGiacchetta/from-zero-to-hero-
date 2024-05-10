import math 
import numpy as np 
import matplotlib.pyplot as plt
from utils import Value, draw_dot, lol

#input
x1 = Value(2.0, label = 'x1')
x2 = Value(0.0, label = 'x2')
#weights
w1 = Value(-3.0, label = 'w1')
w2 = Value(1.0, label = 'w2')
#bias
b = Value(6.8813735870195432, label = 'b')

x1w1 = x1*w1; x1w1.label = 'x1*w1'
x2w2 = x2*w2; x2w2.label = 'x2*w2'
x1w1x2w2 = x1w1 + x2w2; x1w1x2w2.label = 'x1*w1 + x2*w2'
n = x1w1x2w2 + b; n.label = 'n'
o = n.tanh(); o.label = 'o'
o.backward()
draw_dot(o).render('output_tanh', view=True)


x1w1 = x1*w1; x1w1.label = 'x1*w1'
x2w2 = x2*w2; x2w2.label = 'x2*w2'
x1w1x2w2 = x1w1 + x2w2; x1w1x2w2.label = 'x1*w1 + x2*w2'
n = x1w1x2w2 + b; n.label = 'n'
#----- #cambiamo qui --> rompi la tanh in due equ. equivalenti --> dovremmo ottenre gli stessi riusltati ma un grafo più lungo
e = (2*n).exp(); e.label = 'e' 
o = (e-1)/(e+1); o.label = 'o' 
#-----
o.backward()
draw_dot(o).render('output_tanh1', view=True)




'''
x1.grad = w1.data * x1w1.grad
w1.grad = x1.data * x1w1.grad
x2.grad = w2.data * x2w2.grad
w2.grad = x2.data * x2w2.grad
o._backward() #propaga questo a tanh
draw_dot(o).render('output1', view=True)
n._backward()
b._backward()
x1w1x2w2._backward()
x1w1._backward()
x2w2._backward()
o.backward()
draw_dot(o).render('output2', view=True)
'''






