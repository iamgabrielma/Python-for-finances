import urllib2
from urllib2 import urlopen
import time
import re

def getDataFromYahooForIbex35(stock): 

	link = "http://finance.yahoo.com/q?s="+stock
	getSourceCode = urllib2.urlopen(link).read()

	# grabs the price using regex
	p = re.search('(?<=rep.mc">)\d+\.\d*', getSourceCode)
	output = p.group(0)

	if output <= '16.00':
		print 'REPSOL (REP.MC):', output, 'COMPRAR'
	elif output >= '18.50':
		print 'REPSOL (REP.MC):', output, 'VENDER'
	else:
		print 'REPSOL (REP.MC):', output, 'MANTENER'

	# calls function every 5 minutes.
	while True:
		time.sleep(60*5)
		getDataFromYahooForIbex35(stock)


getDataFromYahooForIbex35('REP.MC')
