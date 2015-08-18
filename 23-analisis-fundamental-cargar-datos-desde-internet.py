import matplotlib.pyplot as plt
import numpy as np
import urllib2
#ESTO ES PARA UNIX TIME
import matplotlib.dates as mdates

def representacionGrafica(accion):

	urlAVisitar = 'http://chartapi.finance.yahoo.com/instrument/1.0/' +accion+ '/chartdata;type=quote;range=10y/csv'
	# EXPLICAR UNIX TIME PARA 10 DIAS O MENOS
	#anything greater than 10days is legible time but under 10days is unix time
	
	codigoFuente = urllib2.urlopen(urlAVisitar).read()

	datosAccion = []
	separarCodigoFuente = codigoFuente.split('\n')

	for linea in separarCodigoFuente:
		separarLineas = linea.split(',')
		if len(separarLineas) == 6:
			if 'values' not in linea and 'labels' not in linea:
				datosAccion.append(linea)


	date, closep, highp, lowp, openp, volume = np.loadtxt(datosAccion, delimiter=',', unpack=True, converters = { 0: mdates.strpdate2num('%Y%m%d')})

	plt.plot_date(date,closep,'-',label='Precio')

	plt.xlabel('Numeros en X')
	plt.ylabel('Variable importante en Y')
	plt.title('Titulo del grafico\n subtitulo aqui')

	plt.legend()
	plt.show()

representacionGrafica('KO')
