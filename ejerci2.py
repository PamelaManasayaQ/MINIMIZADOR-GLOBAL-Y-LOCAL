import numpy as np
import matplotlib.pyplot as plt

# Definir la función f(x) = |x|
def f(x):
    return np.abs(x)

# Generar un rango de valores de x
x = np.linspace(-5, 5, 500)

# Evaluar la función en los puntos x
y = f(x)

# Punto crítico x = 0
critical_point = [0]
critical_value = [f(0)]

# Crear el gráfico
plt.figure(figsize=(8, 6))
plt.plot(x, y, label=r"$f(x) = |x|$", color="black")
plt.scatter(critical_point, critical_value, color="black", zorder=5)  # Resaltar el punto crítico
plt.text(0, f(0) + 0.5, r"$x^* = 0$", fontsize=10, color="brown", ha="center")  # Anotación en el punto crítico
plt.title("Gráfico de la función $f(x)$ con punto crítico")
plt.axhline(0, color="gray", linewidth=0.8, linestyle="--")
plt.axvline(0, color="gray", linewidth=0.8, linestyle="--")
plt.legend(fontsize=12)
plt.grid(alpha=0.3)
plt.xlabel("$x$", fontsize=12)
plt.ylabel("$f(x)$", fontsize=12)
plt.show()
