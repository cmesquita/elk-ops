def getTimeStamp():
	timestampNOW = pytime.ctime()
	return timestampNOW
	
def getRunningServerNames():
	# only returns the currently running servers in the domain
	return domainRuntimeService.getServerRuntimes()
 
def getAppStatus():
	domainConfig()
	return cmo.getAppDeployments()
