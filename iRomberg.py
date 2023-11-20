import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

def trapezcomp(funcion, a, b, n):
    h = (b - a) / n
    x = a
    In = funcion.subs('x', a)
    for k in range(1, n):
        x = x + h
        In += 2 * funcion.subs('x', x)
    return (In + funcion.subs('x', b)) * h * 0.5

def romberg(funcion, a, b, p):
    I = np.zeros((p, p))
    for k in range(0, p):
        I[k, 0] = trapezcomp(funcion, a, b, 2 ** k)
        for j in range(0, k):
            I[k, j + 1] = (4 ** (j + 1) * I[k, j] - I[k - 1, j]) / (4 ** (j + 1) - 1)
    return I

expresion = input("Introduce la funcion en terminos de x ( +, -, *, /, **, (, ) ):")
a = float(input("Introduce el valor de 'a': "))
b = float(input("Introduce el valor de 'b': "))
x = sp.symbols('x')
funcion = sp.sympify(expresion)

# Obtener los valores de las aproximaciones de Romberg
approximations = romberg(funcion, a, b, 5)
area_aproximada = approximations[-1][-1]  # Último valor de la aproximación

print("Área aproximada bajo la curva:", area_aproximada)

# Crear puntos para graficar la función
x_vals = np.linspace(a - 0.5, b + 0.5, 100)  # Valores de x para la función
y_vals = [funcion.subs('x', val) for val in x_vals]

x_v = np.linspace(a, b, 100)
y_v = [float(funcion.subs('x', val)) for val in x_v]

plt.plot(x_vals, y_vals, label='Funcion')
plt.plot(x_v, y_v, label='Romberg')
plt.scatter([a], funcion.subs('x', a), color="red")
plt.scatter([b], funcion.subs('x', b), color="red")
plt.fill_between(x_v, 0, y_v, where=(x_v >= a) & (x_v <= b), alpha=0.5, color='gray', label='Area bajo la curva')
plt.title("Grafica")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid()
plt.show()


