import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

def cuadratura(a,b,n,w,z,funcion):
    aux = ((b-a)/2)
    aux2 = ((b+a)/2)
    resultado2 = 0.0
    for i in range(n):
        resultado = aux*z[i]+aux2
        resultado1 = funcion.subs(x,resultado)
        resultado2 += w[i]*resultado1
    area = aux * resultado2
    print(f"La integral es aproximadamente igual a: {area}")

expresion = input("Introduce la funcion en terminos de x ( +, -, *, /, **, (, ) ):" )
x = sp.symbols('x')

funcion = sp.sympify(expresion)

a = float(input("Introduce el valor de 'a': "))
b = float(input("Introduce el valor de 'b': "))
n = int(input("Introduce el numero de puntos del 2 al 6 (n): "))

w = [0.0] * n
z = [0.0] * n

if n == 2:
    w[0]=1.0
    w[1]=w[0]
    z[0]=-0.5773502692
    z[1]=(z[0]*-1)
    cuadratura(a,b,n,w,z,funcion)
if n == 3:
    w[2]=0.55555
    w[0]=w[2]
    w[1]=0.88888
    z[0]=-0.7745966692
    z[1]=0
    z[2]=(z[0]*-1)
    cuadratura(a,b,n,w,z,funcion)
if n == 4:
    w[3]=0.3478548451
    w[0]=w[3]
    w[2]=0.6521451549
    w[1]=w[2]
    z[0]=-0.8611363116
    z[1]=-0.3399810436
    z[2]=(z[1]*-1)
    z[3]=(z[0]*-1)
    cuadratura(a,b,n,w,z,funcion)
if n == 5:
    w[4]=0.2369268851
    w[0]=w[4]
    w[3]=0.4786286705
    w[1]=w[3]
    w[2]=0.56888
    z[0]=-0.9061798459
    z[1]=-0.5384693101
    z[3]=(z[3]*-1)
    z[4]=(z[0]*-1)
    cuadratura(a,b,n,w,z,funcion)
if n == 6:
    w[5]=0.1713244924
    w[0]=w[5]
    w[4]=0.3607615730
    w[1]=w[4]
    w[3]=0.4679139346
    w[2]=w[3]
    z[0]=-0.9324695142
    z[1]=-0.6612093865
    z[2]=-0.2386191861
    z[3]=(z[1]*-1)
    z[4]=(z[2]*-1)
    z[5]=(z[0]*-1)
    cuadratura(a,b,n,w,z,funcion)

x_v1 = np.linspace(a-0.5, b+0.5, 100) # Valores de x para la funcion
y_v1 = [funcion.subs(x, val) for val in x_v1]

x_v = np.linspace(a, b, 100)
y_v = [float(funcion.subs(x, val)) for val in x_v]

plt.plot(x_v1, y_v1,label='Funcion')
plt.plot(x_v, y_v,label='Cuadratura')
plt.scatter([a],funcion.subs(x,a),color="red")
plt.scatter([b],funcion.subs(x,b),color="red")
plt.fill_between(x_v, 0, y_v, where=(x_v >= a) & (x_v <= b), alpha=0.5, color='gray', label='Area bajo la curva')
plt.title("Grafica")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid()
plt.show()