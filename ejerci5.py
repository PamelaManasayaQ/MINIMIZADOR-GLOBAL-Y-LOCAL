import numpy as np
import matplotlib.pyplot as plt
def f(x):
    return np.sin(x)**2

x = np.linspace(0, 2*np.pi, 500)
y = f(x)

min_points = [0, np.pi]
min_values = [f(0), f(np.pi)]

plt.figure(figsize=(8, 6))
plt.plot(x, y, label=r"$f(x) = \sin^2(x)$", color="black")
plt.scatter(min_points, min_values, color="red", zorder=5) 
plt.text(0, f(0) - 0.05, r"$x = 0$", fontsize=12, color="brown", ha="center")
plt.text(np.pi, f(np.pi) - 0.05, r"$x = \pi$", fontsize=12, color="brown", ha="center")
plt.title(r"Gráfico de la función $f(x) = \sin^2(x)$ en el intervalo $[0, 2\pi]$", fontsize=14)
plt.xlabel("$x$", fontsize=12)
plt.ylabel("$f(x)$", fontsize=12)
plt.axhline(0, color="gray", linewidth=0.8, linestyle="--")
plt.axvline(0, color="gray", linewidth=0.8, linestyle="--")
plt.legend(fontsize=12)
plt.grid(True)
plt.show()
