import matplotlib.pyplot as plt
import numpy as np


x = np.arange(-0.1, np.log(20), 0.1)


def f(x):
    y = np.sinh(x)
    return y


def ReglaSimpson(a, b, n):

    h = (b - a) / n
    x = np.linspace(a, b, n+1)
    y = f(x)
    
    integral = 0
    for i in range(0, n-1, 2):  
        integral += h/3 * (y[i] + 4*y[i+1] + y[i+2])
    
    return np.pi * integral

a = 0
b = np.log(20)
n = 4000 

solucion = ReglaSimpson(a, b, n)
print(solucion)



fig, (ax3,ax1, ax2,) = plt.subplots(1, 3, figsize=(12, 4))


ax1.plot(x,f(x), label='y = sinh(x)')
ax1.axhline(0, color='black', linewidth=0.5)
ax1.axvline(0, color='black', linewidth=0.5)

ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_title(u"$\ Gráfica\ de\ la\ función\ y\ =\ Sinh(x)$")

footer_text= f"$\ El\ volumen\ del\ sólido\ de\ revolución$\n $es\ aproximadamente:\ {solucion}$"
ax1.text(-0.75, -0.3, footer_text, transform=ax2.transAxes,fontsize=12, ha='center')

ax2.set_title(u"$\ Región\ encerrada\ por\ y\ =\ Sinh(x)$")
ax2.fill_between(x, f(x), color = "blue",alpha=0.2)
ax2.fill_between(x, -f(x), color = "blue", alpha=0.2)
ax2.axhline(0, color='black', linewidth=0.5)
ax2.axvline(0, color='black', linewidth=0.5)

ax3.axis('off')


theta = np.linspace(0, 2 * np.pi, 100)
X, Z = np.meshgrid(x, theta)
Y = f(x)

X_cartesian = Y * np.cos(Z)
Y_cartesian = Y * np.sin(Z)

ax = fig.add_subplot(131, projection='3d')
ax.plot_surface(X_cartesian, Y_cartesian, X, cmap='viridis')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title(u'$Sólido\ de\ revolución\ generado$\n $Por\ y\ =\ Sinh(x)\ alrededor\ del\ eje\ x$')

plt.tight_layout()
plt.show()









