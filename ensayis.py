import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Definir la función y = sinh(x)
def sinh(x):
    return np.sinh(x)

# Crear un rango de valores de x desde 0 hasta ln(20)
x = np.linspace(0, np.log(20), 100)

# Calcular los valores correspondientes de y
y = sinh(x)

# Crear una gráfica 2D de la región
plt.figure()
plt.plot(x, y, label='y = sinh(x)')
plt.fill_between(x, 0, y, alpha=0.2)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Región encerrada por y = sinh(x)')

# Calcular los puntos para crear el sólido de revolución
theta = np.linspace(0, 2 * np.pi, 100)
X, Z = np.meshgrid(x, theta)
Y = sinh(X)

# Convertir las coordenadas de la malla en coordenadas cartesianas
X_cartesian = Y * np.cos(Z)
Y_cartesian = Y * np.sin(Z)

# Crear una gráfica 3D del sólido de revolución
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X_cartesian, Y_cartesian, X, cmap='viridis')

# Configurar etiquetas de los ejes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Sólido de revolución generado por y = sinh(x) alrededor del eje X')

# Mostrar la gráfica
plt.show()
