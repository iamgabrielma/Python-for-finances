import matplotlib.pyplot as plt
import numpy as np
import urllib2
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from matplotlib.finance import candlestick_ohlc
#anado modulo
from matplotlib import style

style.use('fivethirtyeight')

def distanciasMaximosMinimos(maximos, minimos):
	return maximos-minimos

def representacionGrafica(accion):

	'''DISTRIBUCION DE LOS GRAFICOS'''
	'''anadidos titulos, labels y sharex'''
	ax1 = plt.subplot2grid((6,1), (0,0), rowspan=1, colspan=1)
	plt.title(accion)
	plt.ylabel('Max-Min')
	ax2 = plt.subplot2grid((6,1), (1,0), rowspan=4, colspan=1, sharex=ax1)
	plt.ylabel('Precios')
	ax3 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1)
	plt.ylabel('Volumen')

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
	candlestick_ohlc(ax2, ohlc, width=0.4, colorup='g', colordown='r')

	'''DISTANCIAS ENTRE MAXIMOS Y MINIMOS'''
	distMinMax = list(map(distanciasMaximosMinimos, highp, lowp))
	# ANADIDO LINEWIDTH
	ax1.plot_date(date,distMinMax,'-',linewidth = 1)

	'''VOLUMEN'''
	ax3.fill_between(date,volume, facecolor='#0079a3', alpha=0.4)
	ax3.plot(date,volume,linewidth = 1)


	'''REPRESENTACION GRAFICA'''

	#plt.xlabel('Numeros en X')
	#plt.ylabel('Variable importante en Y')
	#plt.title('Titulo del grafico\n subtitulo aqui')

	'''ESTILO GENERAL'''
	'''anadido 45grados a anos y estilo general'''
	for label in ax3.xaxis.get_ticklabels():
		label.set_rotation(45)

	ax1.yaxis.set_major_locator(mticker.MaxNLocator(nbins=4, prune='lower'))
	ax2.yaxis.set_major_locator(mticker.MaxNLocator(nbins=7, prune='upper'))
	ax3.yaxis.set_major_locator(mticker.MaxNLocator(nbins=5, prune='upper'))

	plt.subplots_adjust(left=0.09, bottom=0.11,right=0.94,top=0.93,wspace=0.2,hspace=0.5)
	#ax2.axes.yaxis.set_ticklabels([])
	'''quitamos las labels de axis x ya que con ellas en x3 basta'''
	plt.setp(ax1.get_xticklabels(), visible=False)
	plt.setp(ax2.get_xticklabels(), visible=False)

	plt.legend()
	plt.show()

representacionGrafica('KO')
