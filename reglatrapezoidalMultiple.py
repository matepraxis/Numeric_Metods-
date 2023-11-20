#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 14:07:28 2023

@author: mario
"""


import numpy as np


def Reglatrapezoidal(f, a, b, n):
    
    h = (b - a) / n
    
    
    sumatoria = 0
    for i in range(1, n):
        x_i = a + i * h
        sumatoria = sumatoria + f(x_i)
    
    
    resultado = (h / 2) * (f(a) + 2*sumatoria + f(b))
    
    return h,resultado


def f(x):
    return (1 + (x / 2)**2)**2  


def tabla(N):
    a = 0
    b = 2
        
    for i in  range(2,N+1):
       h, inte = Reglatrapezoidal(f, a, b, i)
       inte2=np.pi*inte
       Error=np.abs(((11.72861-(np.pi*inte))/11.72861)*100.0)
       print(f"{i} \t {h} \t {inte2} \t {Error}" )



a = 0
b = 2
n = 10  

resultado = Reglatrapezoidal(f, a, b, n)[1]
Volumen=resultado*np.pi
print(f"Resultado de la integral: {resultado}", f"Luego el Volumen es: {Volumen} ")
Error=((11.72861-Volumen)/11.72861)*100.0
print(f"El error porcential es {Error}")



# x0=0.0
# h=1/3
# for i in range(n+1):
#     print(x0+i*h)
    
# tabla(10)
