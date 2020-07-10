import numpy as np
import time as ti
import pyvisa as visa


# Se fija en que puerto recibe datos.
RM = visa.ResourceManager()

# Te muestra los puertos.
intr = RM.list_resources()

# Elijo el puerto correcto
multimetro = RM.open_resource(intr[2])


# Resetea el multimetro a fabrica.
multimetro.write('*RST')
multimetro.write('*CLS')

# Hacemos que mida con menos precision.
multimetro.write('CONF:FRES 100,0.1')

T = np.array([])
R = np.array([])
i = 0

# Hago mediciones y guardo el tiempo y resistencia.
while i >= 0:
    # Hace una medicion.
    stringM = multimetro.query('MEAS:FRES?')

    # Asigna la medicion.
    R = np.append(R, np.array([float(stringM)]))
    if i == 0:

        # Defino un tiempo inicial.
        tz = ti.time()
    t = ti.time() - tz

    # Array del tiempo.
    T = np.append(T, np.array([t]))

    # Break luego de medir por tantos segundos.
    if t > 150:
        break
    i = i + 1

# Array con tiempos y resistencias.
S = np.column_stack((T, R))

# Guardo los datos en un csv.
np.savetxt("D2-C3R-1.csv", S, delimiter=",")
