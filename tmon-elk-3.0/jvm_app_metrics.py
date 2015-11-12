#jvm_metrics.py
import time as pytime
user = "weblogic"
password = "manager1"
connect_string = "t3://192.168.47.205:7001"

# connecting weblogic	 
connect(user,password,connect_string)

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
	ServerState()
	getHTTPSessions()