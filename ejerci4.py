import numpy as np
import matplotlib.pyplot as plt

# Definir la función f(x, y)
def f(x, y):
    return x**2 + y**2

# Crear un rango de valores para x e y
x = np.linspace(-1, 1, 500)
y = np.linspace(-1, 1, 500)

# Crear los valores de la función
Z = f(x, 0)  # Evaluar en y = 0
Z_y = f(0, y)  # Evaluar en x = 0

# Graficar la función
plt.figure(figsize=(8, 6))
plt.plot(x, Z, label=r"$f(x, 0) = x^2 + 0^2$", color="black")
plt.plot(np.zeros_like(y), y, label=r"$f(0, y) = 0^2 + y^2$", color="black")
plt.scatter(0, 0, color="red", zorder=5)  # Resaltar el mínimo global en (0, 0)

# Título y etiquetas
plt.title(r"Gráfico de la función $f(x, y) = x^2 + y^2$", fontsize=14)
plt.xlabel("$x$", fontsize=12)
plt.ylabel("$f(x, y)$", fontsize=12)

# Mostrar el valor del mínimo
plt.text(0, 0.5, r"$Mínimo Global (0, 0)$", fontsize=12, color="brown", ha="center")

# Configuración adicional
plt.axhline(0, color="gray", linewidth=0.8, linestyle="--")
plt.axvline(0, color="gray", linewidth=0.8, linestyle="--")
plt.legend(fontsize=12)
plt.grid(True)

# Mostrar la gráfica
plt.show()
