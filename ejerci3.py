import numpy as np
import matplotlib.pyplot as plt

# Definir la función f(x) = sin(x)
def f(x):
    return np.sin(x)

# Crear un arreglo de puntos x en el intervalo [0, pi]
x = np.linspace(0, np.pi, 500)

# Calcular los valores de f(x)
y = f(x)

# Determinar los puntos críticos (en este caso, los extremos del intervalo)
x_min = [0, np.pi]
y_min = [f(0), f(np.pi)]

# Crear la gráfica
plt.figure(figsize=(8, 6))
plt.plot(x, y, label=r"$f(x) = \sin(x)$", color="black")
plt.scatter(x_min, y_min, color="red", zorder=5)  # Resaltar los puntos mínimos globales
plt.text(0, f(0) - 0.1, r"$x = 0$", fontsize=12, color="brown", ha="center")
plt.text(np.pi, f(np.pi) - 0.1, r"$x = \pi$", fontsize=12, color="brown", ha="center")

# Personalización de la gráfica
plt.title("Gráfico de la función $f(x) = \sin(x)$ en el intervalo $[0, \pi]$")
plt.axhline(0, color="gray", linewidth=0.8, linestyle="--")
plt.axvline(0, color="gray", linewidth=0.8, linestyle="--")
plt.legend(fontsize=12)
plt.grid(alpha=0.3)
plt.xlabel("$x$", fontsize=12)
plt.ylabel("$f(x)$", fontsize=12)

# Mostrar la gráfica
plt.show()
