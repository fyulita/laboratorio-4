import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as sci
import Datos
import Campo_y_Temperatura


# Defino algunas variables en los limites que desee.
T = Campo_y_Temperatura.Temp[:]
B = Campo_y_Temperatura.Brem[:]
Time = Campo_y_Temperatura.Time[:]
H = Campo_y_Temperatura.Hco[:]


# Ajuste del campo remanente.
def ajuste(t, tc, gamma, a):
    b = a * ((np.abs(tc - t)) ** gamma)
    return b


guess = np.array([2.88883054e+02, 6.53564885e-01, 2.79477492e-02])
values, cov = sci.curve_fit(ajuste, T, B, p0=guess, bounds=([240., 0.1, 0.01], [300., 1., 0.05]))

print(values)

# Grafico el campo remanente en funcion de la temperatura promedio con el ajuste.
plt.figure('Campo Remanente')
plt.plot(T, B, 'ro', label=r"$Datos$")
plt.plot(T, ajuste(T, values[0], values[1], values[2]), 'bo', label=r"$Ajuste$")
plt.grid()
plt.legend()
plt.xlabel(r"$T \ (K)$")
plt.ylabel(r"$B_{rem} \ (V)$")
plt.savefig('Campo_Remanente_{}.png'.format(Datos.arch))

# Grafico el campo coercitivo en funcion de la temperatura promedio.
plt.figure('Campo Coercitivo')
plt.plot(T, H, 'co')
plt.grid()
plt.xlabel(r"$T \ (K)$")
plt.ylabel(r"$H_{co} \ (V)$")
plt.savefig('Campo_Coercitivo_{}.png'.format(Datos.arch))

# Grafico la temperatura promedio en funcion del tiempo promedio.
plt.figure('Temperatura')
plt.plot(Time, T, 'go')
plt.grid()
plt.xlabel(r'$t \ (s)$')
plt.ylabel(r'$T \ (K)$')
plt.savefig('Temperatura_{}.png'.format(Datos.arch))
