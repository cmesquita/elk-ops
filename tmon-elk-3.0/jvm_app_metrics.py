#jvm_metrics.py
import time as pytime
user = "weblogic"
password = "manager1"
connect_string = "t3://192.168.47.205:7001"

# connecting weblogic	 
connect(user,password,connect_string)

def getTest():
	domainConfig()
	try:
		cd('/AppDeployments/benefitsa')
		print pwd()
	except WLSTException,e:
		print "fudeo"
		#print e.Message()
	

def getHTTPSessions():
	pwdstr = pwd()[:15]
	if pwdstr != 'domainRuntime:/':
		domainRuntime()
	serverNames = getRunningServerNames()
	#apps = getAppStatus()
	apps=cmo.getAppDeployments()
        pwdstr = pwd()[:15]
        if pwdstr != 'domainRuntime:/':
                domainRuntime()
	for app in apps:	
		for server in serverNames:
			try:
				appName = str(app.getName())
				serverName = str(server.getName())
				pathName = '/ServerRuntimes/' + serverName + '/ApplicationRuntimes/' + str(appName) + '/ComponentRuntimes/' + serverName + '_/' + str(appName)
				print pwd()
				print pathName
				cd(pathName)
				print pwd()
				print "agora sim"
				print "OpenSessionsCurrentCount: " +  str(cmo.getOpenSessionsCurrentCount())	
			except WLSTException,e:
				print "fudeo"
				#print "Ignoring exception " + e.getMessage()
	
def ServerState():
	servers = getRunningServerNames()
	domainRuntime()
	sign="###"
	activecount=0
	problemcount=0
	cd('domainRuntime:/AppRuntimeStateRuntime/AppRuntimeStateRuntime')
	apps = getAppStatus()
	for app in apps:
		for server in servers:
			cd("/ServerLifeCycleRuntimes/" + server.getName())
			serverState = cmo.getState()
			if serverState == "RUNNING" and server.getName()!="ADMINHOST"  :
				cd('domainRuntime:/AppRuntimeStateRuntime/AppRuntimeStateRuntime')
				currentState = str(cmo.getCurrentState(app, server.getName()))
				if currentState == "STATE_ACTIVE":
					print '%25s,  %25s :\033[1;32m %1s %15s \033[0m' % (app,server.getName(),sign,currentState)
	

def getRunningServerNames():
	domainConfig()
	return cmo.getServers()

def getAppStatus():
	cd('domainRuntime:/AppRuntimeStateRuntime/AppRuntimeStateRuntime')
	return cmo.getApplicationIds()

if __name__== "main":
	getHTTPSessions()
	#getTest()
