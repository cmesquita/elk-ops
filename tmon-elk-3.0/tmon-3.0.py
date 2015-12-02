import  lib.tmon_configparser as configparser
import  modules.tmon_metrics as metrics

def tmonMetricsMonitor():
	tmonLog = str(metrics.getGCmetrics(configparser.getServerList())) +  str(metrics.getJVMmetrics(configparser.getServerList() ,configparser.getAdminUser() , configparser.getAdminPass() , configparser.getConnectString()))
	return tmonLog

#def tmonStackMonitor():

if __name__== "main":
	file = open("tmon.log","w")
 	file.write(   tmonMetricsMonitor()  )
	file.close()
