import matplotlib.pyplot as plt
import Datos


# Grafico la figura de histeresis para cada tanda y la guardo.
for i in range(0, Datos.L):
    plt.figure(i)
    plt.plot(Datos.data[i][:, 3], Datos.data[i][:, 4], 'bo')
    plt.grid()
    plt.xlabel(r"$H \ (V)$")
    plt.ylabel(r"$B \ (V)$")
    plt.savefig("Figura_{}_{}.png".format(Datos.arch, i))
