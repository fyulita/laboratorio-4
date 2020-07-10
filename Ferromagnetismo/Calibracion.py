import numpy as np
import scipy.optimize as sci


# Calibracion del Pt100
T = np.array([77, 2.8 + 273.15, 21 + 273.15])  # K
V = np.array([21.6, 107.4, 115.8]) * 1e-3  # V


def cal(v, a, b, c):
    t = a * (v ** 2) + b * v + c
    return t


values, cov = sci.curve_fit(cal, V, T)
