import matplotlib.pyplot as plt
import numpy as np
import urllib2
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from matplotlib.finance import candlestick_ohlc

def representacionGrafica(accion):

	#fig = plt.figure()
	#ax1 = plt.subplot2grid((1,1),(0,0))
	'''DISTRIBUCION DE LOS GRAFICOS'''
	ax1 = plt.subplot2grid((6,1), (0,0), rowspan=1, colspan=1)
	ax2 = plt.subplot2grid((6,1), (1,0), rowspan=4, colspan=1)
	ax3 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1)

	'''EXTRACCION DE DATOS'''
	urlAVisitar = 'http://chartapi.finance.yahoo.com/instrument/1.0/' +accion+ '/chartdata;type=quote;range=10y/csv'
	
	codigoFuente = urllib2.urlopen(urlAVisitar).read()

	datosAccion = []
	separarCodigoFuente = codigoFuente.split('\n')

	for linea in separarCodigoFuente:
		separarLineas = linea.split(',')
		if len(separarLineas) == 6:
			if 'values' not in linea and 'labels' not in linea:
				datosAccion.append(linea)


	date, closep, highp, lowp, openp, volume = np.loadtxt(datosAccion, delimiter=',', unpack=True, converters = { 0: mdates.strpdate2num('%Y%m%d')})

	'''VELAS JAPONESAS'''
	x = 0
	y = len(date)
	ohlc = []

	while x < y:
		agregar = date[x],closep[x],highp[x],lowp[x],openp[x],volume[x]
		ohlc.append(agregar)
		x +=1
	#candlestick_ohlc(ax1, ohlc, width=0.4, colorup='g', colordown='r')
	candlestick_ohlc(ax2, ohlc, width=0.4, colorup='g', colordown='r')


	'''REPRESENTACION GRAFICA'''

	plt.xlabel('Numeros en X')
	plt.ylabel('Variable importante en Y')
	plt.title('Titulo del grafico\n subtitulo aqui')

	plt.legend()
	plt.show()

representacionGrafica('KO')
