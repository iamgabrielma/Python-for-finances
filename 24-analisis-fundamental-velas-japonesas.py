import matplotlib.pyplot as plt
import numpy as np
import urllib2
import matplotlib.dates as mdates
#ANADO
import matplotlib.ticker as mticker
from matplotlib.finance import candlestick_ohlc

def representacionGrafica(accion):

	fig = plt.figure()
	ax1 = plt.subplot2grid((1,1),(0,0))

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
	candlestick_ohlc(ax1, ohlc, width=0.4, colorup='g', colordown='r')


	'''REPRESENTACION GRAFICA'''
	#CON ESTA LINEA ACTIVADA SALE UN GRAFICO ADICIONAL PREVIO
	#plt.plot_date(date,closep,'-',label='Precio')

	plt.xlabel('Numeros en X')
	plt.ylabel('Variable importante en Y')
	plt.title('Titulo del grafico\n subtitulo aqui')

	plt.legend()
	plt.show()

representacionGrafica('KO')
