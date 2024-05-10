from utils import Value, draw_dot, lol


a = Value(2.0, label = 'a')
b = Value(-3.0, label = 'b')
c = Value(10.0, label = 'c')
e = a*b; e.label = 'e'
d = e + c; d.label = 'd'
f = Value(-2.0, label = 'f')
L = d * f; label = 'L'
L.grad = 1.0
f.grad = 4.0
d.grad = -2.0
c.grad = -2.0
e.grad = -2.0
a.grad = -2.0 * -3.0
b.grad = -2.0 * 2.0

#python non sa come sammare due value object 
print(a.__add__(b))
print("a+b = ", a+b) #posso fare direttamente così perchè l'ho definita come funzione base della classe

print(a.__mul__(b))
print("a*b = ", a*b)
print("c = ", c)


print(d)
print(d._prev) #è il set dei figli, ovvero (a*b) e c
print(f'd è calcolata sulla base della {d._op} di questi due valori {d._prev} (che sono i suoi figli)')




agga = lol()


gugu = draw_dot(L)
gugu.render('output', view=True)


#ONE STEP DI OTTIMIZZAZIONE
a.data += 0.01 * a.grad
b.data += 0.01 * b.grad
c.data += 0.01 * c.grad
f.data += 0.01 * f.grad

e = a * b
d = e + c
L = d * f
print(L.data)
