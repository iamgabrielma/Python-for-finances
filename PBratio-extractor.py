import time
import urllib2
from urllib2 import urlopen

miCarteraEnSP500 = ['a', 'aa', 'aapl', 'abbv', 'abc', 'abt', 'ace', 'aci', 'acn', 'act', 'adbe', 'adi', 'adm', 'adp']


def yahooAnalisisFundamental(stock):
	try:
		sourceCode = urllib2.urlopen('http://finance.yahoo.com/q/ks?s='+stock).read()
		print 'price to book ratio: ', stock

	except Exception, e:
		print 'error, para el valor: ', stock, str(e)

for cadaStock in miCarteraEnSP500:
	yahooAnalisisFundamental(cadaStock)
