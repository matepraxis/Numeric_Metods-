#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 21:33:05 2023

@author: mario
"""

import numpy as np
import matplotlib.pyplot as plt


def simpson_13(f, x0, x1, x2):
    h= (x2 - x0)/2
    
    inte=(h/3.0)*(f(x0) + 4*f(x1) + f(x2))
    
    return inte

print("Intral de seno ente 0 y pi/2", simpson_13(np.sin, 0, np.pi/4 , np.pi/2.0))


def simpson_38(f, x0, x1, x2, x3):
    h= (x3 - x0)/3
    
    inte=(3.0*h/8.0)*(f(x0) + 3*f(x1) + 3*f(x2) + f(x3))
    
    return inte


h=(np.pi/2 - 0)/3.0

x0=0.0
x1=x0+h
x2=x0+2*h
x3=x0+3*h

print("h=",h)
print("Intral de seno ente 0 y pi/2", simpson_38(np.sin, x0, x1 ,  x2, x3))




x = np.array([x0, x1 ,  x2, x3])  
y = np.sin(x)

for i in range(len(x)):
    print("(", x[i], ",", y[i], ")")



V = np.vander(x, increasing=True)


coeficientes = np.linalg.solve(V, y)
print("Los coeficientes: ", coeficientes[::-1])


P=np.poly1d(coeficientes[::-1])

print("El polinomio: ")
print(P)



xp = np.linspace(min(x), max(x), 100)
yp = P(xp)


plt.plot(xp, yp, label='Polinomio Interpolante', linestyle='--')
plt.plot(xp, np.sin(xp), label='Seno', linestyle='-')

plt.scatter(x, y, label='Puntos de Interpolación', color='red', marker='o')



plt.xlabel('x')
plt.ylabel('y')
plt.title('Interpolación de Puntos')
plt.grid(ls="dashed")
plt.legend()



