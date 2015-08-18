import random
import matplotlib.pyplot as plt
from matplotlib import style

'''min ejecucion matplotlib'''
# fig = plt.figure()
# plt.show()

'''anadimos random info'''
def crearPlots():
	xs = []
	ys = []

	for i in range(10):
		x = i
		y = random.randrange(10)

		xs.append(x)
		ys.append(y)
	return xs, ys

'''entiendo que el primer (6,1) es dividir en 6 cachos en x y 1 cacho en y, por eso son alargados como lo ancho del programa, el segundo (0,0) es la posicion que toman, como ax2 tiene rowspan 4 tenemos que empezar ax3 en 5,0)'''

ax1 = plt.subplot2grid((6,1),(0,0),rowspan=1,colspan=1)
ax2 = plt.subplot2grid((6,1), (1,0), rowspan=4, colspan=1)
ax3 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1)
#fig = plt.figure()

x,y = crearPlots()
ax1.plot(x,y) #crea datos en 1
ax2.plot(x,y) #crea datos en 2
ax3.plot(x,y) #crea datos en 3

plt.show()

