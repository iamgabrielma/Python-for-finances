import urllib2
import time

accionAExtraer = 'KO', 'CAT', 'TSLA', 'AMZN'

def extraerDatos(accion):

	try:

		archivo = accion + '.txt'
		urlAVisitar = 'http://chartapi.finance.yahoo.com/instrument/1.0/'+accion+'/chartdata;type=quote;range=1y/csv'
		codigoFuente = urllib2.urlopen(urlAVisitar).read()
		separarFuente = codigoFuente.split('\n')
		#print codigoFuente

		for cadaLinea in separarFuente:
			separarLineas = cadaLinea.split(',')

			if len(separarLineas) == 6:
				if 'values' not in cadaLinea:
					guardarArchivo = open(archivo, 'a')
					lineaAEscribir = cadaLinea + '\n'
					guardarArchivo.write(lineaAEscribir)
		print 'Extrayendo', accion
		time.sleep(1)
		print 'Extraido', accion

	except Exception, e:

		print 'No ha funcionado, hay un problema en:', str(e)

#extraerDatos(accionAExtraer)

for cadaAccion in accionAExtraer:
	extraerDatos(cadaAccion)
