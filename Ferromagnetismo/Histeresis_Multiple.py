import matplotlib.pyplot as plt
import numpy as np
import Datos
import Campo_y_Temperatura


# Importo la temperatura promedio para cada figura de histeresis.
T = Campo_y_Temperatura.Temp

# Tandas que quiero graficar.
t = np.array([])

# Grafico varias figuras de histeresis juntas.
plt.figure('Histeresis Multiple')
plt.plot(Datos.data[t[0]][:, 3], Datos.data[t[0]][:, 4], 'm-', label=r"$T = {}K$".format(int(T[t[0]])))
plt.plot(Datos.data[t[1]][:, 3], Datos.data[t[1]][:, 4], 'c-', label=r"$T = {}K$".format(int(T[t[1]])))
plt.plot(Datos.data[t[2]][:, 3], Datos.data[t[2]][:, 4], 'b-', label=r"$T = {}K$".format(int(T[t[2]])))
plt.plot(Datos.data[t[3]][:, 3], Datos.data[t[3]][:, 4], 'g-', label=r"$T = {}K$".format(int(T[t[3]])))
plt.plot(Datos.data[t[4]][:, 3], Datos.data[t[4]][:, 4], 'y-', label=r"$T = {}K$".format(int(T[t[4]])))
plt.plot(Datos.data[t[5]][:, 3], Datos.data[t[5]][:, 4], 'r-', label=r"$T = {}K$".format(int(T[t[5]])))
plt.grid()
plt.legend()
plt.xlabel(r"$H \ (V)$")
plt.ylabel(r"$B \ (V)$")
plt.savefig("Histeresis_Multiple_{}.png".format(Datos.arch))
