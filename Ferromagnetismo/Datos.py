import numpy as np
import pandas as pd
import Calibracion


# Archivo que quiero leer
arch = 3

# Leo los archivos .csv.
datos = pd.read_csv("Data_{}.csv".format(arch), skiprows=1, decimal=",", delimiter=";")

# Tomo sus valores en un array.
datos = datos.values

# Columna 0: Tiempo Unix.
# Columna 1: Voltaje 5V.
# Columna 2: Voltaje Pt100.
# Columna 3: Voltaje Resistencia (H).
# Columna 4: Voltaje Circuito Invertido (-B).

# Repito la primera medicion asi mi array tiene un multiplo de 100 columnas.
datos = np.vstack((datos[0, :], datos))

# Cambio la primera columna para que sea el tiempo absoluto.
datos[:, 0] = datos[:, 0] - datos[0, 0]

# Cambio la columna 4 para que no este invertido.
datos[:, 4] = -datos[:, 4]

# Cambio la columna 2 para que sea la temperatura en Kelvins segun la calibracion.
datos[:, 2] = Calibracion.values[0] * (datos[:, 2] ** 2) + Calibracion.values[1] * datos[:, 2] + Calibracion.values[2]

# Separo mis datos en tandas de 100. En x especifico la tanda, en y especifico la medicion y en z especifico
# que se midio.
L = int(np.shape(datos)[0] / 100)    # Tandas

data = np.split(datos, L)

# Centro la figura de histeresis.
for i in range(0, L):
    data[i][:, 3] = data[i][:, 3] - 0.5 * (np.max(data[i][:, 3]) + np.min(data[i][:, 3]))
    data[i][:, 4] = data[i][:, 4] - 0.5 * (np.max(data[i][:, 4]) + np.min(data[i][:, 4]))
