import numpy as np


def simpson13(f, a, b, n):
    h = (b - a) / n
    
    
    suma = f(a) + f(b)
    
    # Suma los términos pares
    for i in range(1, n, 2):
        suma += 4 * f(a + i * h)
    
    # Suma los términos impares
    for i in range(2, n - 1, 2):
        suma += 2 * f(a + i * h)
    
    
    resultado = (h / 3) * suma
    
    return h, resultado

def f(x):
    return x**2 



a = 0
b = 2
n = 32   # Número de subintervalos (debe ser par)


def tabla(N):
    a = 0
    b = 2
        
    for i in  range(2,N+1, 2):
       h, inte = simpson13(f, a, b, i)
       inte2=np.pi*inte
       Error=np.abs(((11.72861-(np.pi*inte))/11.72861)*100.0)
       print(f"{i} \t {h} \t {inte2} \t {Error}" )





resultado = simpson13(f, a, b, n)[1]
Volumen=resultado*np.pi
print(f"Resultado de la integral: {resultado}", f"Luego el Volumen es: {Volumen} ")
Error=((11.72861-Volumen)/11.72861)*100.0
print(f"El error porcential es {Error}")


