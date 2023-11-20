import matplotlib.pyplot as plt
import numpy as np


x = np.arange(-0.1, 1.1, 0.01)


def f(x):
    y = x**2
    return y

def f2(x):
    y = x
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
b = 2
n = 4000 

solucion = ReglaSimpson(a, b, n)



fig, (ax3,ax1,ax2) = plt.subplots(1, 3, figsize=(12, 4))

ax1.plot(x, f(x))
ax1.plot(x, f2(x))
ax1.plot(0, f(0), 'ro') 
ax1.plot(1, f2(1), 'ro')
  

ax1.set_title(u"$\ Gráfica\ de\ los\ lugares\ geométricos$")
ax1.set_xlabel('x')
ax1.set_ylabel('y')

ax1.axhline(0, color='black', linewidth=0.5)
ax1.axvline(0, color='black', linewidth=0.5)
footer_text= f"$\ El\ volumen\ del\ sólido\ de\ revolución$\n $es\ aproximadamente: {solucion}$"
ax1.text(-0.75, -0.3, footer_text, transform=ax2.transAxes,fontsize=12, ha='center')


ax2.fill_betweenx(f(x), 0, x, color='blue', alpha=0.5)
ax2.fill_betweenx(f(x), 0, -x, color='blue', alpha=0.5)
ax2.set_xlabel('Eje X')
ax2.set_ylabel('Eje Y')
ax2.set_title(u"$\ Sólido\ de\ Revolución:\ y\ =\ x^2\ (alrededor\ del\ eje\ Y)$")

ax1.axhline(0, color='black', linewidth=0.5)
ax1.axvline(0, color='black', linewidth=0.5)

ax3.axis('off')

theta = np.linspace(0, 2.*np.pi, 100)
r, th = np.meshgrid(x, theta)
X = r * np.cos(th)
Y = r * np.sin(th)
Z = r**2

ax = fig.add_subplot(131, projection='3d')
ax.plot_surface(X, Y, Z, color='b')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title(u"$\ Sólido\ de\ revolución$\n $generado\ por\ y\ =\ x^2$")

plt.tight_layout()

plt.show()










