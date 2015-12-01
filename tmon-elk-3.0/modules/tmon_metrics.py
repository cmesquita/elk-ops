import time as pytime
from wlstModule import *

def getGCmetrics():
	connect('weblogic','manager1','t3://192.168.47.205:7003')
	custom()
	cd('java.lang')
	cd('java.lang:type=GarbageCollector,name=G1 Old Generation')
	getCollectionTime = get('CollectionTime')
	getCollectionCount = get('CollectionCount')
	gcmetrics = str(getCollectionTime) + ' ' + str(getCollectionCount)
	return gcmetrics

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
	getOpenSessionsCurrentCount = ""
        serverNames = getRunningServerNames()
        apps = getAppStatus()
	pwdstr = pwd()[:15]
        if pwdstr != 'domainRuntime:/':
                domainRuntime()
        for app in apps:
                for server in serverNames:
                        try:
                                appName = str(app.getName())
                                serverName = str(server.getName())
                                #pathName = '/ServerRuntimes/' + serverName + '/ApplicationRuntimes/' + str(appName) + '/ComponentRuntimes/' + serverName + '_/' + str(appName)
                                pathName = '/ServerRuntimes/' + serverName + '/ApplicationRuntimes/' + appName + '/ComponentRuntimes/' + serverName + '_/' + appName
				cd(pathName)
                                OpenSessionsCurrentCount = str(cmo.getOpenSessionsCurrentCount())
				getOpenSessionsCurrentCount = str(OpenSessionsCurrentCount) + ' ' + getOpenSessionsCurrentCount
                        except WLSTException,e:
                                pass
                                #print "Ignoring exception " + e.getMessage()
		return getOpenSessionsCurrentCount
	
'''
def getGCElapsedTime():
	customPathGCOld = "java.lang:type=GarbageCollector,name=G1 Old Generation"
	customPathGCYoung = "java.lang:type=GarbageCollector,name=G1 Young Generation"
	customConnectString = ""
	user = "weblogic"
	password = "manager1"
	connect_string = "t3://192.168.47.205:7001"
	custom()
'''
	
def getTimeStamp():
	timestampNOW = pytime.ctime()
	return timestampNOW
	
def getRunningServerNames():
	# only returns the currently running servers in the domain
	return domainRuntimeService.getServerRuntimes()
 
def getAppStatus():
	domainConfig()
	return cmo.getAppDeployments()

	
if __name__== "main":
#we are still working in progress
	#x = getJVMmetrics() + getOpenSockets() + getHTTPSessions() + getTimeStamp()
	#x = getGCmetrics()
	#print x	
#getHTTPSessions()
#getGCElapsedTime()
	disconnect()
