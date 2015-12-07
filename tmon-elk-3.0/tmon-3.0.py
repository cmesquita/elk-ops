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
	for args in paramServerList:
		profile_server = args.split()
		server_name = profile_server[0]
		app_name = profile_server[5]
		tmonLog.append( [ server_name , app_name  ,  str(metrics.getGCmetrics( args ) ) ,  str(metrics.getJVMmetrics( args , paramAdminUser , paramAdminPass , paramConnectString ) ) , str(metrics.getHTTPSessions( args , paramAdminUser , paramAdminPass , paramConnectString )) , str(metrics.getOpenSockets( args , paramAdminUser , paramAdminPass , paramConnectString ) ) , str(metrics.getTimeStamp() )])
	
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
			tmonLog2.append( [ j[0] , j[5] , hogging_cnt , stuck_cnt , z[0] ] )
	return tmonLog2
	
		

if __name__== "main": 

	file = open("tmon.log","w")
	log = ''
	for content_tmon in tmonMetricsMonitor():
		log = ''
		for log_entry in content_tmon:
			log += str(log_entry) + ' '
		file.write( log )
		file.write( "\n")
	file.close()	

	
	file = open("tmon2.log","w")
	log = ''
	for content_tmon2 in tmonStackMonitor():
		log = ''
		for log_entry in content_tmon2:
			log += str(log_entry) + ' '
		file.write(  log )
		file.write( "\n")
	file.close()
