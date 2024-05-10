from utils import Value, draw_dot

a = Value(2.0)
b = Value(-3.0)
c = Value(10.0)
#python non sa come sammare due value object 
print(a.__add__(b))
print("a+b = ", a+b) #posso fare direttamente così perchè l'ho definita come funzione base della classe

print(a.__mul__(b))
print("a*b = ", a*b)

print("c = ", c)
d = a*b + c
print(d)
print(d._prev) #è il set dei figli, ovvero (a*b) e c
print(f'd è calcolata sulla base della {d._op} di questi due valori {d._prev} (che sono i suoi figli)')


gugu = draw_dot(d)
gugu.render('output', view=True)