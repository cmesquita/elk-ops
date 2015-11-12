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
        getheapSize = ""
        if pwdstr != 'domainRuntime:/':
                domainRuntime()
        for name in serverNames:
                print 'Now checking '+name.getName()
                try:
                        cd("/ServerRuntimes/"+name.getName()+"/JVMRuntime/"+name.getName())
                        heapSize = cmo.getHeapSizeCurrent()
                        getheapSize = str(heapSize)  + ' ' + getheapSize
                except WLSTException,e:
                        # this typically means the server is not active, just ignore
                        # pass
                        print "Ignoring exception " + e.getMessage()
        return getheapSize
        
def getOpenSockets():
	serverNames = getRunningServerNames()
	pwdstr = pwd()[:15]
	getOpenSocketsCurrentCount = ""
	if pwdstr != 'domainRuntime:/':
		domainRuntime()
	for name in serverNames:
		print 'Now checking '+name.getName()
		try:
			cd("/ServerRuntimes/"+name.getName())
			OpenSocketsCurrentCount = cmo.getOpenSocketsCurrentCount()	
			getOpenSocketsCurrentCount = str(OpenSocketsCurrentCount) + ' ' + getOpenSocketsCurrentCount
		except WLSTException,e:
			# this typically means the server is not active, just ignore
			# pass
			print "Ignoring exception " + e.getMessage()
	return getOpenSocketsCurrentCount


def getHTTPSessions():
	pwdstr = pwd()[:15]
	if pwdstr != 'domainRuntime:/':
		domainRuntime()
	serverNames = getRunningServerNames()
	apps = getAppStatus()
	for app in apps	
		for server in serverNames:
			print 'Now checking '+ server.getName() + ' ' + app
			#try:
				#cd('ApplicationRuntimes/lms/ComponentRuntimes/lms01_/lmsa')
			#	cd("/ServerRuntimes/"+name.getName()+"/ApplicationRuntimes/"+app()/ComponentRuntimes
				print "/ServerRuntimes/" + name.getName() + "/ApplicationRuntimes/" +app "/ComponentRuntimes"
				#cd("/ApplicationRuntimes/"+name.getName())
				#OpenSessionCurrentCount = cmo.getOpenSessionsCurrentCount()
				#print OpenSessionCurrentCount
			#except WLSTException,e:
				# this typically means the server is not active, just ignore
				# pass
			#	print "Ignoring exception " + e.getMessage()
	
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
	return timestampNOW
	
def getRunningServerNames():
	# only returns the currently running servers in the domain
	return domainRuntimeService.getServerRuntimes()
 
 def getAppStatus():
	cd('domainRuntime:/AppRuntimeStateRuntime/AppRuntimeStateRuntime')
	return cmo.getApplicationIds()
 
if __name__== "main":
#we are still working in progress
	x = getJVMmetrics() + getOpenSockets()
	print x	
#getHTTPSessions()
#getGCElapsedTime()
	getTimeStamp()
	disconnect()

