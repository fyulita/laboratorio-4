import numpy as np
import Datos


# Hallo el valor de B cuando H = 0, el valor de H cuando B = 0, el tiempo promedio y la temperatura
# promedio para cada tanda.
Brem = np.array([])
Hco = np.array([])
Temp = np.array([])
Time = np.array([])
for i in range(0, Datos.L):
    Hmin = np.min(np.abs(Datos.data[i][:, 3]))  # Donde H se anula.
    Bmin = np.min(np.abs(Datos.data[i][:, 4]))  # Donde B se anula.
    B = np.abs(Datos.data[i][np.where(np.abs(Datos.data[i]) == Hmin)[0][0], 4])     # Valor de B donde H se anula.
    H = np.abs(Datos.data[i][np.where(np.abs(Datos.data[i]) == Bmin)[0][0], 3])     # Valor de H donde B se anula.
    Brem = np.append(Brem, B)
    Hco = np.append(Hco, H)
    Temp = np.append(Temp, np.mean(Datos.data[i][:, 2]))
    Time = np.append(Time, np.mean(Datos.data[i][:, 0]))
