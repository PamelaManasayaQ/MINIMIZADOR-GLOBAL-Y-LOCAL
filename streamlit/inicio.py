import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Título
st.title("Métodos de Optimización")
st.subheader("Universidad Nacional del Altiplano")
st.subheader("Facultad de Ingeniería Estadística e Informática")
st.write("\n")
st.subheader("Trabajo Encargado - N° 010")
st.subheader("Métodos de Optimización - OPTIMIZACIÓN NO LINEAL")
st.write("\n")
st.markdown("**Docente:** Fred Torres Cruz")
st.markdown("**Autor:** Heydi Pamela Manasaya Quispe")
st.markdown("**GITHUB:** [Link](https://github.com/PamelaManasayaQ/optimizacion-no-lineal)")
st.write(f"**Fecha:** {np.datetime64('today', 'D')}")

st.write("\n")
st.markdown('---')

# Ejercicio 1
st.markdown("### **EJERCICIO 1**")
st.write("Dada la función \(f(x) = x^2 - 4x + 5\), verificamos si los puntos \(x = 2\) y \(x = 0\) son minimizadores globales o locales.")

st.markdown("#### 1. Función dada:")
st.latex(r"f(x) = x^2 - 4x + 5")

st.write("Esta es una función cuadrática con apertura hacia arriba, lo que garantiza la existencia de un **mínimo global**.")

st.markdown("#### 2. Encontrar el vértice (mínimo global):")
st.latex(r"x^* = -\frac{b}{2a}")

st.write("Para \(a = 1\), \(b = -4\), y \(c = 5\):")
st.latex(r"x^* = \frac{4}{2} = 2")

st.write("El valor de la función en \(x = 2\) es:")
st.latex(r"f(2) = (2)^2 - 4(2) + 5 = 1")

st.write("Por lo tanto, \(x = 2\) es un **minimizador global**.")

st.markdown("#### 3. Evaluación en \(x = 0\):")
st.latex(r"f(0) = 5")

st.write("Comparando con el valor mínimo global \(f(2) = 1\), tenemos que \(f(0) > f(2)\), por lo tanto:")
st.write("- \(x = 0\) no es un **minimizador global**.")
st.write("- Tampoco es un **minimizador local**.")

st.markdown("#### 4. Conclusión:")
st.write("- \(x = 2\): Es un **minimizador global** de \(f(x)\).")
st.write("- \(x = 0\): No es un minimizador (ni global ni local).")

st.write("\n")
st.markdown('---')

# Ejercicio 2
st.markdown("### **EJERCICIO 2**")
st.write("Analizar la función \( f(x) = |x| \) y determinar si tiene un mínimo global o local en \( x = 0 \).")

st.markdown("#### 1. Función:")
st.latex(r"f(x) = |x|")

st.markdown("#### 2. Identificación del mínimo:")
st.write("La función tiene una forma en 'V', con vértice en \(x = 0\).")
st.write("Para \(x \geq 0\), la función es \(f(x) = x\), y para \(x < 0\), la función es \(f(x) = -x\).")

st.markdown("#### 3. Verificación de mínimo global:")
st.write("Para cualquier \( x \neq 0 \), se tiene que \(f(x) > 0\). Por lo tanto, el valor mínimo de la función ocurre en \(x = 0\).")

st.markdown("#### 4. Conclusión:")
st.write("El punto \(x = 0\) es un **mínimo global** de la función \(f(x) = |x|\), ya que \(f(0) = 0\) es el valor más bajo que puede tomar la función en todo su dominio.")

st.write("\n")
st.markdown('---')

# Ejercicio 3
st.markdown("### **EJERCICIO 3**")
st.write("Teorema de Weierstrass y la función \( f(x) = \sin(x) \) en el intervalo \( [0, \pi] \).")

st.markdown("#### Teorema de Weierstrass:")
st.write("Si una función \( f(x) \) es continua y está acotada en un conjunto convexo \( D \), entonces existe al menos un mínimo global en ese conjunto.")

st.markdown("#### Paso 1: Verificación de la continuidad")
st.write("La función \( f(x) = \sin(x) \) es continua en el intervalo \( [0, \pi] \).")

st.markdown("#### Paso 2: Verificación de la acotación")
st.write("La función \( f(x) = \sin(x) \) está acotada en \( [0, \pi] \), con \( 0 \leq \sin(x) \leq 1 \).")

st.markdown("#### Paso 3: Aplicación del Teorema de Weierstrass")
st.write("Dado que la función es continua y acotada, aplicamos el teorema, lo que garantiza la existencia de un mínimo global.")

st.markdown("#### Paso 4: Determinación del mínimo global")
st.latex(r"f(0) = \sin(0) = 0 \quad y \quad f(\pi) = \sin(\pi) = 0")

st.write("Por lo tanto, el mínimo global de \( f(x) = \sin(x) \) en \( [0, \pi] \) es \( 0 \), y ocurre en \( x = 0 \) y \( x = \pi \).")

st.markdown("#### Conclusión:")
st.write("La función tiene un mínimo global en \( x = 0 \) y \( x = \pi \), con \( f(x) = 0 \) en estos puntos.")

st.write("\n")
st.markdown('---')

# Ejercicio 4
st.markdown("### **EJERCICIO 4**")
st.write("Considera la función \( f(x, y) = x^2 + y^2 \) con la restricción \( x^2 + y^2 \leq 1 \). Determina el mínimo global.")

st.markdown("#### 1. Definición de la función:")
st.latex(r"f(x, y) = x^2 + y^2")

st.write("Esta función está definida en el dominio \( x^2 + y^2 \leq 1 \), que corresponde a un círculo unitario en el plano \( xy \).")

st.markdown("#### 2. Puntos críticos:")
st.write("Las derivadas parciales son \( \frac{\partial f}{\partial x} = 2x \) y \( \frac{\partial f}{\partial y} = 2y \).")
st.write("Igualando ambas derivadas a cero, encontramos que \( x = 0 \) y \( y = 0 \), por lo que el único punto crítico es el origen.")

st.markdown("#### 3. Evaluación de la función en el dominio:")
st.write("La función tiene su mínimo global en el origen, ya que \( f(0, 0) = 0 \) es el valor más bajo que puede tomar la función dentro del dominio.")

st.markdown("#### Conclusión:")
st.write("El mínimo global de \( f(x, y) = x^2 + y^2 \) en el dominio \( x^2 + y^2 \leq 1 \) es \( f(0, 0) = 0 \).")
