import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.optimize as sci


# Leo los archivos .csv.
datos1 = pd.read_csv("D2-C3-1.csv", header=None)
datos2 = pd.read_csv("D2-C3R-1.csv", header=None)

# Tomo sus valores en un array.
datos1 = datos1.values
datos2 = datos2.values


# Esta funcion me suaviza los datos x promediando cada dato con los "window" siguientes.
def smooth(x, window=10):
    for i in range(0, len(x)):
        if i + window > len(x) - 1:
            x[i] = np.average(x[i:len(x)])
        else:
            x[i] = np.average(x[i:i + window + 1])

    return x


# Defino los tiempos y resistencias medidas por las columnas del array "datos".
t1 = datos1[:, 0]   # s
R1 = datos1[:, 1]   # Ohms
t2 = datos2[:, 0]
R2 = datos2[:, 1]


# Calibro el Pt100.
t = np.array([296.65, 273.15, 77])  # K
r = np.array([109, 101, 20.4])      # Ohms


def cal(R, a, b, c):
    T = a * R ** 2 + b * R + c
    return T

    
popt, pcov = sci.curve_fit(cal, r, t)

a = popt[0]
b = popt[1]
c = popt[2]


# Defino la temperatura. Sale de la calibracion del Pt100.
T1 = a * R1 ** 2 + b * R1 + c   # K
T2 = a * R2 ** 2 + b * R2 + c


# Grafico.
plt.figure(1)
plt.plot(t1, T1, "bo", label=r"$Al1$")
plt.plot(t2, T2, "ro", label=r"$Al2$")
plt.grid()
plt.legend()
plt.xlabel(r"$t \ (s)$")
plt.ylabel(r"$T \ (K)$")
plt.savefig("Grafico-temperatura-forma.png")
plt.show()


# Defino la derivada temporal de x usando arrays de los valores de x a tiempo ti.
def timeder(x, ti):
    xdot = np.array([])
    i = 0

    while i <= len(x) - 1:
        if i == len(x) - 1:
            xdot = np.append(xdot, np.array([xdot[i - 1]]))
        else:
            xdot = np.append(xdot, np.array([(x[i + 1] - x[i]) / (ti[i + 1] - ti[i])]))
        i = i + 1

    return xdot


# Defino las derivadas de la temperatura.
def Tdot(T, t):
    Tdot = timeder(T, t)
    return Tdot


n1 = 2.609       # moles
n2 = 14.808
n3 = 3.674
n3R = 3.463
A1 = 4183.1e-6        # Area en m^2
A2 = 13389e-6
A3 = 6054e-6
A3R = 5947.6e-6
R = 8.314       # Constante de Gas en J / (mol * K).
ThetaD_Cu = 343        # Temperatura de Debye del Cu en K.
ThetaD_Al = 428        # Temperatura de Debye del Al en K.
a = 0.77
b = 0.26        # Constantes
c = 9.17


# Temperatura de Einstein del Cu en K.
def ThetaE(T, Deb):
    ThetaE = Deb * (a + b * np.exp(-c * T / Deb))
    return ThetaE


# Calor especifico en J / K.
def Cl(T, Deb):
    Cl = 3 * R * ((ThetaE(T, Deb) / T) ** 2) * np.exp(Deb / T) / ((np.exp(Deb / T) - 1) ** 2)
    return Cl


# Finalmente la densidad de calor por tiempo en W.
def densidad_Qdot(n, T, Deb, t, A):
    Qdot = -n * Cl(T, Deb) * Tdot(T, t) / A
    return Qdot


# Suavizo los datos.
def Qdot_suave(n, T, Deb, t, A, window):
    Qdot = smooth(densidad_Qdot(n, T, Deb, t, A), window)
    return Qdot


# Grafico. Al final no suavizo los datos porque no hace falta.
plt.figure(2)
plt.semilogx(T1 - 77, Qdot_suave(n3, T1, ThetaD_Al, t1, A3, 1) / 1000, "bo", label=r"$Al1$")
plt.semilogx(T2 - 77, Qdot_suave(n3R, T2, ThetaD_Al, t2, A3R, 1) / 1000, "ro", label=r"$Al2$")
plt.grid()
plt.legend(loc=2)
plt.xlabel(r"$\Delta T \ (K)$")
plt.ylabel(r"$\frac{\dot{Q}}{A} \ \left( \frac{kW}{m^2} \right)$")
plt.savefig("Grafico-calor-forma.png")
plt.show()
