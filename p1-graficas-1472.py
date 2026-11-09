import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print("jose solis NC 1472")

# Listas de videojuegos con 4 elementos cada una:
# (Nombre, copias vendidas en millones, es multijugador, año lanzamiento)
mc  = ['Minecraft', 300, True, 2011]
gta = ['GTA V', 190, True, 2013]
tet = ['Tetris', 100, False, 1984]
wii = ['Wii Sports', 82.9, True, 2006]
pub = ['PUBG', 75, True, 2017]

# Creamos la lista de listas (conformando la tabla)
lista_juegos = [mc, gta, tet, wii, pub]

# Utilizar pandas para organizar (DataFrame)
# A cada columna le ponemos nombre
df_juegos = pd.DataFrame(lista_juegos, columns=["Nombre", "Copias_Vendidas", "Es_Multijugador", "Año_Lanzamiento"])
print(df_juegos)

# Crear el archivo CSV y guardarlo
# df_juegos.to_csv("videojuegos.csv", index=False)

# 1. Gráfica de líneas (x: Nombre, y: Copias Vendidas)
plt.plot(df_juegos["Nombre"], df_juegos["Copias_Vendidas"])
plt.title("Gráfica de videojuegos 1472")
plt.xlabel("Nombre del videojuego")
plt.ylabel("Copias vendidas (Millones)")
plt.show()

# 2. Gráfica de puntos (Scatter)
plt.scatter(df_juegos["Nombre"], df_juegos["Copias_Vendidas"])
plt.show()

# 3. Gráfica de barras sencilla
plt.bar(df_juegos["Nombre"], df_juegos["Copias_Vendidas"])
plt.title("Videojuegos 1472")
plt.xlabel("Los juegos")
plt.ylabel("Copias vendidas (Millones)")
plt.show()

# 4. Ordenar la gráfica de barras de manera descendente
df_juegos_ordenar = df_juegos.sort_values("Copias_Vendidas", ascending=False)
plt.bar(df_juegos_ordenar["Nombre"], df_juegos_ordenar["Copias_Vendidas"])
plt.show()

# 5. Coloreando la gráfica de barras ordenada (5 elementos = 5 colores)
plt.bar(df_juegos_ordenar["Nombre"], df_juegos_ordenar["Copias_Vendidas"], 
        color=["b", "g", "c", "m", "y"])
plt.show()

# 6. Gráfica de pastel (Pie chart)
plt.pie(df_juegos["Copias_Vendidas"], labels=df_juegos["Nombre"])
plt.show()

print("jose solis nc 1472")