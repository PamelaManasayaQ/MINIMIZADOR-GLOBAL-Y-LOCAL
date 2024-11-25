import numpy as np
import matplotlib.pyplot as plt
def f(x):
    return x**2 - 4*x + 5

x = np.linspace(-1, 5, 500)

y = f(x)

critical_points = [0, 2]
critical_values = [f(c) for c in critical_points]

plt.figure(figsize=(8, 6))
plt.plot(x, y, label=r"$f(x) = x^2 - 4x + 5$", color="black")
plt.scatter(critical_points, critical_values, color="black", zorder=5)  # Resaltar puntos críticos
plt.text(0, f(0) + 0.5, r"$x = 0$", fontsize=10, color="brown", ha="center")
plt.text(2, f(2) - 0.5, r"$x^* = 2$", fontsize=10, color="brown", ha="center")
plt.title("Gráfico de la función $f(x)$ con puntos críticos")
plt.axhline(0, color="gray", linewidth=0.8, linestyle="--")
plt.axvline(0, color="gray", linewidth=0.8, linestyle="--")
plt.legend(fontsize=12)
plt.grid(alpha=0.3)
plt.xlabel("$x$", fontsize=12)
plt.ylabel("$f(x)$", fontsize=12)
plt.show()
