#jvm_metrics.py
user = "weblogic"
password = "passw0rd"
connect_string = "t3://172.16.3.125:7001"

# connecting weblogic	 
connect(user,password,connect_string)

def getJVMmetrics():
	while 1:
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
        
def getOpenSockets():
	while 1:
        serverNames = getRunningServerNames()
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
	while 1:
        serverNames = getRunningServerNames()
        domainRuntime()
        for name in serverNames:
            print 'Now checking '+name.getName()
            try:
              cd("/ServerRuntimes/"+name.getName())
              OpenSessionCurrentCount = cmo.getOpenSessionsCurrentCount()
			  print OpenSessionCurrentCount
            except WLSTException,e:
              # this typically means the server is not active, just ignore
              # pass
                print "Ignoring exception " + e.getMessage()
	
def getGCElapsedTime():
	
def getTimeStamp():
	
def getRunningServerNames():
	# only returns the currently running servers in the domain
	return domainRuntimeService.getServerRuntimes()
 
if __name__== "main":
	getJVMmetrics()
	disconnect()
