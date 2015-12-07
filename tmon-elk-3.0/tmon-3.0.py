import  lib.tmon_configparser as configparser
import  modules.tmon_metrics as metrics
import	modules.tmon_threads as threads

def tmonMetricsMonitor():
	# parameter from tmon3.0.conf
	paramServerList = configparser.getServerList()
	paramAdminUser 	= configparser.getAdminUser()
	paramAdminPass	= configparser.getAdminPass()
	paramConnectString = configparser.getConnectString()
	tmonLog = []	
	
	# tmonLog variable which has the data to be printed in the log file
	for i in paramServerList:
		j = i.split()
		tmonLog.append( [ j[0] , j[4] ,  str(metrics.getGCmetrics( i ) ) ,  str(metrics.getJVMmetrics( i , paramAdminUser , paramAdminPass , paramConnectString ) ) , str(metrics.getHTTPSessions( i , paramAdminUser , paramAdminPass , paramConnectString )) , str(metrics.getOpenSockets( i , paramAdminUser , paramAdminPass , paramConnectString ) ) , str(metrics.getTimeStamp() )])
	
	# this is log print format for jvm related
	#container || app || gc time || gc count || heap usage || http sessions cnt || open sockets cnt || timestamp 
	return tmonLog

def tmonStackMonitor():
	paramServerList = configparser.getServerList()
	tmonLog2 = []
	for i in paramServerList:
		j = i.split()
		hogging_cnt = threads.getThreadStucksCount( i )[1]
		stuck_cnt = threads.getThreadStucksCount( i )[2]
		for z in threads.getThreadStackHash( i ,  threads.getThreadStucksCount( i )[0] ):
			tmonLog2.append( [ j[0] , j[4] , hogging_cnt , stuck_cnt , z[0] ] )
	return tmonLog2
	
		

if __name__== "main": 

	file = open("tmon.log","w")
	for content_tmon in tmonMetricsMonitor():
		file.write( str(content_tmon) )
		file.write( "\n")
	file.close()	

	file = open("tmon2.log","w")
	for content_tmon2 in tmonStackMonitor():
		file.write(  str(content_tmon2) )
		file.write( "\n")
	file.close()
