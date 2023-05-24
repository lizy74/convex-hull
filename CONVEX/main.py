import numpy as np
import matplotlib.pyplot as plt
import random

def distancia(punto1, punto2):
    return np.sqrt((punto2[0] - punto1[0]) ** 2 + (punto2[1] - punto1[1]) ** 2)

def envoltura_convexa(puntos):
    if len(puntos) < 3:
        return puntos
    envoltura = []
    izquierdo = min(puntos, key=lambda p: p[0])
    envoltura.append(izquierdo)
    punto_actual = izquierdo
    while True:
        siguiente_punto = puntos[0]
        for punto in puntos[1:]:
            orientacion = (siguiente_punto[0] - punto_actual[0]) * (punto[1] - punto_actual[1]) - \
                          (siguiente_punto[1] - punto_actual[1]) * (punto[0] - punto_actual[0])
            if np.array_equal(siguiente_punto, punto_actual) or orientacion > 0 or \
                    (orientacion == 0 and distancia(punto_actual, punto) > distancia(punto_actual, siguiente_punto)):
                siguiente_punto = punto
        envoltura.append(siguiente_punto)
        punto_actual = siguiente_punto
        if np.array_equal(punto_actual, izquierdo):
            break
    return envoltura

def generar_puntos_aleatorios():
    num_puntos = random.randint(1, 100)
    x_min, x_max = 0, 1  # Rango para la coordenada x
    y_min, y_max = 0, 1  # Rango para la coordenada y
    puntos = np.random.uniform(low=[x_min, y_min], high=[x_max, y_max], size=(num_puntos, 2))
    return puntos

def actualizar_grafico(evento):
    global puntos, envoltura
    puntos = generar_puntos_aleatorios()
    envoltura = envoltura_convexa(puntos)
    ax.clear()
    ax.scatter(puntos[:, 0], puntos[:, 1], color='blue', label='PUNTOS')
    ax.plot(np.array(envoltura + [envoltura[0]])[:, 0], np.array(envoltura + [envoltura[0]])[:, 1], color='green', label='PUNTOS CONVEXOS')
    ax.fill(np.array(envoltura)[:, 0], np.array(envoltura)[:, 1], color='green', alpha=0.3)
    ax.set_title('CONVEX HULL', fontsize=16)
    ax.legend()
    plt.draw()

# Generar puntos aleatorios
puntos = generar_puntos_aleatorios()
envoltura = envoltura_convexa(puntos)

# Crear gráfica
fig, ax = plt.subplots(figsize=(9, 7))  # Ajustar el tamaño de la figura
ax.scatter(puntos[:, 0], puntos[:, 1], color='blue', label='PUNTOS')
ax.plot(np.array(envoltura + [envoltura[0]])[:, 0], np.array(envoltura + [envoltura[0]])[:, 1], color='green', label='PUNTOS CONVEXOS')
ax.fill(np.array(envoltura)[:, 0], np.array(envoltura)[:, 1], color='green', alpha=0.3)
ax.set_title('CONVEX HULL', fontsize=16)
ax.legend()

# Crear botón para generar nuevos puntos
ax_boton = plt.axes([0.8, 0.02, 0.19, 0.05])  # Ajustar las dimensiones del botón
boton = plt.Button(ax_boton, 'Generar Nueva Gráfica')
boton.on_clicked(actualizar_grafico)
# Mostrar la gráfica
plt.show()
