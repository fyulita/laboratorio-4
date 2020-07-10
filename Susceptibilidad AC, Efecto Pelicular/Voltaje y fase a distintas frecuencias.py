import numpy as np
import matplotlib.pyplot as plt


f = np.array([15, 30, 36.63, 40, 100, 200, 366.3, 420, 500, 750, 2000, 3663, 5000, 7500, 9000, 10000, 20000])  # Hz

VB = np.append(np.append(1e-9 * np.array([210, 539, 735, 840]), 1e-6 * np.array([3.6, 10.6, 26.92, 36.65, 45.07,
                                                                                 91.7])),
               1e-3 * np.array([0.5283, 1.3733, 2.111, 3.526, 4.397, 4.988, 11.66]))
# V. Voltaje con Al1 A.K.A. Slim Shady(Barra delgada)

VBerr = np.append(1e-9 * np.array([2, 2, 7, 20, 100, 100, 20, 10, 20, 300]), np.array([0.0001, 0.0001, 0.001, 0.001,
                                                                                       0.001, 0.001, 0.001]))  # V

FB = np.array([-64.5, -51.5, -48.7, -46, -40, -38, -35.96, -34.65, -33.20, -31, -38.77, -52.02, -59.31, -67.75, -71.01,
               -72.75, -82.96])  # Fase con Al1

FBerr = np.array([1, 0.5, 0.4, 1, 2, 0.4, 0.04, 0.03, 0.02, 0.2, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01])

VV = np.append(1e-6 * np.array([0.110, 0.309, 0.430, 0.5, 2.20, 5.79, 11.7, 13.9, 16.61, 25.4, 69.9, 104.07, 192.7]),
               1e-3 * np.array([0.3268, 0.4258, 0.4961, 1.7893]))  # V. Voltaje sin barra

VVerr = np.append(1e-6 * np.array([0.002, 0.009, 0.008, 0.02, 0.05, 0.05, 0.4, 0.5, 0.05, 0.4, 0.1, 0.04, 0.1]),
                  1e-3 * np.array([0.0001, 0.0001, 0.0001, 0.0003]))  # V

FV = np.array([-56, -47, -46.2, -45, -53.5, -65.2, -75.5, -77, -80.4, -85, -95.2, -102.99, -107.89, -115.03, -118.37,
               -120.37, -126.16])  # Fase sin barra

FVerr = np.array([2, 1, 0.8, 3, 2, 0.3, 1.5, 4, 0.2, 1, 0.1, 0.02, 0.02, 0.01, 0.01, 0.01, 0.01])

VBB = np.append(1e-6 * np.array([0.252, 0.79, 1.13, 1.33, 7.2, 24.95, 76.4, 98.6, 136.3]), 1e-3 *
                np.array([0.2879, 1.4386, 3.181, 4.606, 7.355, 9.057, 10.210, 22.80]))
# V. Voltaje con Al2 A.K.A. Average Shady(Barra gruesa)

VBBerr = np.append(1e-6 * np.array([0.002, 0.02, 0.01, 0.3, 0.15, 0.1, 0.8, 0.7]), 1e-3 *
                   np.array([0.0005, 0.0001, 0.001, 0.006, 0.001, 0.001, 0.001, 0.01, 0.01]))  # V

FBB = np.array([-44.6, -30, -27.5, -26, -22, -20.6, -21.6, -22, -23.2, -28.3, -49.95, -63.3, -68.60, -73.95, -75.95,
                -77.04, -83.70])  # Fase con Al2

FBBerr = np.array([0.3, 1, 0.5, 1, 2, 0.2, 0.1, 0.3, 0.2, 0.04, 0.01, 0.1, 0.03, 0.01, 0.01, 0.01, 0.04])


VBx = VB * np.cos(FB * (2 * np.pi / 360))
VBy = VB * np.sin(FB * (2 * np.pi / 360))
VVx = VV * np.cos(FV * (2 * np.pi / 360))
VVy = VV * np.sin(FV * (2 * np.pi / 360))
VBBx = VBB * np.cos(FBB * (2 * np.pi / 360))
VBBy = VBB * np.sin(FBB * (2 * np.pi / 360))


ChipS = (VBy - VVy) / (f * 5.5e-7)       # Chi' Al1
ChippS = (VBx - VVx) / (f * 5.5e-7)      # Chi'' Al1
ChipA = (VBBy - VVy) / (f * 0.0000011)   # Chi' Al2
ChippA = (VBBx - VVx) / (f * 0.0000011)  # Chi'' Al2


plt.errorbar(f / 1000, VB * 1000, VBerr * 1000, None, "ro", label="Al1")
plt.errorbar(f / 1000, VBB * 1000, VBBerr * 1000, None, "bo", label="Al2")
plt.errorbar(f / 1000, VV * 1000, VVerr * 1000, None, "go", label="Sin muestra")
plt.grid()
plt.legend()
plt.xlabel(r"$Frecuencia \ (kHz)$")
plt.ylabel(r"$V_{out} \ (mV)$")
plt.savefig("voltaje_inducido.png")
plt.show()


plt.semilogx(f, np.log(VB), "ro", label="Al1")
plt.semilogx(f, np.log(VBB), "bo", label="Al2")
plt.semilogx(f, np.log(VV), "go", label="Sin muestra")
plt.grid()
plt.legend()
plt.xlabel(r"$Frecuencia \ (dB)$")
plt.ylabel(r"$log(V_{out}) \ (V)$")
plt.savefig("voltaje_inducido_log.png")
plt.show()


plt.semilogx(f, 1 + ChipS, "ro", label="Al1")
plt.semilogx(f, 1 + ChipA, "bo", label="Al2")
plt.grid()
plt.legend()
plt.xlabel(r"$Frecuencia \ (dB)$")
plt.ylabel(r'$\mu´ \ (V\cdot s)$')
plt.savefig('mu´_samples.png')
plt.show()


plt.semilogx(f, 1 + ChippS, "ro", label="Al1")
plt.semilogx(f, 1 + ChippA, "bo", label="Al2")
plt.grid()
plt.legend(loc=2)
plt.xlabel(r"$Frecuencia \ (dB)$")
plt.ylabel(r'$\mu´´ \ (V\cdot s)$')
plt.savefig('mu´´_samples.png')
plt.show()
