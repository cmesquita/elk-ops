import  lib.tmon_configparser as configparser
import  modules.tmon_metrics as metrics
import	modules.tmon_threads as threads

def tmonMetricsMonitor():
	# parameter from tmon3.0.conf
	paramServerList = configparser.getServerList()
	paramAdminUser 	= configparser.getAdminUser()
	paramAdminPass	= configparser.getAdminPass()
	paramConnectString = configparser.getConnectString()
	paramAppName = configparser.getAppName()

	# tmonLog variable which has the data to be printed in the log file
	tmonLog = str(metrics.getGCmetrics( paramServerList ) ) +  str(metrics.getJVMmetrics( paramServerList , paramAdminUser , paramAdminPass , paramConnectString ) ) + str(metrics.getHTTPSessions( paramServerList , paramAdminUser , paramAdminPass , paramConnectString , paramAppName )) + str(metrics.getOpenSockets( paramServerList , paramAdminUser , paramAdminPass , paramConnectString ) ) + str(metrics.getTimeStamp())

	return tmonLog

def tmonStackMonitor():
	paramServerList = configparser.getServerList()
	threads.getThreadStucksCount( paramServerList )

if __name__== "main":
	tmonStackMonitor()
	#file = open("tmon.log","w")
 	#file.write(   tmonMetricsMonitor()  )
	#file.close()
