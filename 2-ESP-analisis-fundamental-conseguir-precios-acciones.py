import urllib2
import time

accionAExtraer = 'KO'

def extraerDatos(accion):
	'''Extraeremos datos de yahoo finance y lo guardaremos en un archivo .txt en nuestro sistema'''

	try:
		archivo = accion + '.txt'
		urlAVisitar = 'http://chartapi.finance.yahoo.com/instrument/1.0/'+accion+'/chartdata;type=quote;range=1y/csv'
		codigoFuente = urllib2.urlopen(urlAVisitar).read()
		separarFuente = codigoFuente.split('\n')

		for cadaLinea in separarFuente:
			separarLineas = cadaLinea.split(',')
			
			if len(separarLineas) == 6:
				if 'values' not in cadaLinea:
					guardarArchivo = open(archivo, 'a') #a for appending
					lineaAEscribir = cadaLinea + '\n'
					guardarArchivo.write(lineaAEscribir)
					
		print 'Extrayendo', accion
		time.sleep(1)
		print 'Extraido', accion

		

	except Exception, e:

		print 'no ha funcionado, problema en: ', str(e)

extraerDatos(accionAExtraer)


