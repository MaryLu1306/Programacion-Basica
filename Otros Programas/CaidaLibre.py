import numpy as np
import matplotlib.pyplot as plt

# Parámetros
v0 = 20  # m/s (velocidad inicial)
g = 9.8  # m/s² (gravedad)
t_max = 2 * v0 / g  # Tiempo total de vuelo (4.08 s)
t = np.linspace(0, t_max, 100)  # División del tiempo en 100 puntos

# Ecuación de altura en función del tiempo
h = v0 * t - 0.5 * g * t**2

# Configuración del gráfico
plt.figure(figsize=(10, 5))
plt.plot(t, h, 'b-', linewidth=2, label='Altura vs. Tiempo')
plt.title('Posición vs. Tiempo', fontsize=14)
plt.xlabel('Tiempo (s)', fontsize=12)
plt.ylabel('Altura (m)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)

# Línea en altura 0 (suelo)
plt.axhline(y=0, color='k', linestyle='-', linewidth=0.5)

# Línea vertical en el tiempo de altura máxima
t_max_height = v0 / g
plt.axvline(x=t_max_height, color='r', linestyle='--', label=f't = {t_max_height:.2f} s (altura máxima)')

# Mostrar leyenda y gráfico
plt.legend()
plt.show()