import  lib.tmon_configparser as configparser
import  modules.tmon_metrics as metrics

def tmonMetricsMonitor():
	paramServerList = configparser.getServerList()
	paramAdminUser 	= configparser.getAdminUser()
	paramAdminPass	= configparser.getAdminPass()
	paramConnectString = configparser.getConnectString()
	paramAppName = configparser.getAppName()

	tmonLog = str(metrics.getGCmetrics( paramServerList ) +  str(metrics.getJVMmetrics( paramServerList , paramAdminUser , paramAdminPass , paramConnectString ) ) + str(metrics.getHTTPSessions( paramServerList , paramAdminUser , paramAdminPass , paramConnectString , paramAppName ))

	return tmonLog

#def tmonStackMonitor():

if __name__== "main":
	file = open("tmon.log","w")
 	file.write(   tmonMetricsMonitor()  )
	file.close()
