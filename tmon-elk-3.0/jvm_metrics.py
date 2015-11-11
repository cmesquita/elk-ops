#jvm_metrics.py
import time as pytime
user = "weblogic"
password = "manager1"
connect_string = "t3://192.168.47.205:7001"

# connecting weblogic	 
connect(user,password,connect_string)

def getJVMmetrics():
	serverNames = getRunningServerNames()
	pwdstr = pwd()[:15]
	if pwdstr != 'domainRuntime:/':
		domainRuntime()
	for name in serverNames:
		print 'Now checking '+name.getName()
		try:
			cd("/ServerRuntimes/"+name.getName()+"/JVMRuntime/"+name.getName())
			heapSize = cmo.getHeapSizeCurrent()
			print heapSize
		except WLSTException,e:
			# this typically means the server is not active, just ignore
			# pass
			print "Ignoring exception " + e.getMessage()
        
def getOpenSockets():
	serverNames = getRunningServerNames()
	pwdstr = pwd()[:15]
	if pwdstr != 'domainRuntime:/':
		domainRuntime()
	for name in serverNames:
		print 'Now checking '+name.getName()
		try:
			cd("/ServerRuntimes/"+name.getName())
			getOpenSocketsCurrentCount = cmo.getOpenSocketsCurrentCount()
			print getOpenSocketsCurrentCount
		except WLSTException,e:
			# this typically means the server is not active, just ignore
			# pass
			print "Ignoring exception " + e.getMessage()

def getHTTPSessions():
	'''
	serverNames = getRunningServerNames()
	domainRuntime()
	for name in serverNames:
		print 'Now checking '+name.getName()
		try:
			cd("/ApplicationRuntimes/"+name.getName())
			OpenSessionCurrentCount = cmo.getOpenSessionsCurrentCount()
			print OpenSessionCurrentCount
		except WLSTException,e:
			# this typically means the server is not active, just ignore
			# pass
			print "Ignoring exception " + e.getMessage()
	'''
def getGCElapsedTime():
	'''
	serverNames = getRunningServerNames()
	domainRuntime()
	for name in serverNames:
	print 'Now checking '+name.getName()
	try:
	cd("/ServerRuntimes/"+name.getName()+"/JVMRuntime/"+name.getName())
	heapSize = cmo.getHeapSizeCurrent()
	print heapSize
	except WLSTException,e:
	# this typically means the server is not active, just ignore
	# pass
	print "Ignoring exception " + e.getMessage()
	'''
def getTimeStamp():
	timestampNOW = pytime.ctime()
	print timestampNOW
	
def getRunningServerNames():
	# only returns the currently running servers in the domain
	return domainRuntimeService.getServerRuntimes()
 
if __name__== "main":
#we are still working in progress
	getJVMmetrics()
	getOpenSockets()
#getHTTPSessions()
#getGCElapsedTime()
	getTimeStamp()
	disconnect()
