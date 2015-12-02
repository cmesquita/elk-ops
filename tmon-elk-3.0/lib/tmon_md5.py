import time as pytime
import md5
import ConfigParser, os

def genMD5( stacktrace ):
	m=md5.new()
	m.update( stacktrace )
	output = m.digest()
	hexoutput = m.hexdigest()
	return hexoutput
