import time as pytime
import md5
import ConfigParser, os

def genMD5( stacktrace ):
	hexoutput = []
	stacklist = []
	for i in stacktrace:
		m=md5.new()
		m.update( i )
		output = m.digest()
		stacklist.append ( [m.hexdigest() , i ] )
	return stacklist
