import  lib.tmon_configparser as configparser
import  modules.tmon_metrics as metrics

def tmonMetricsMonitor():
	return metrics.getGCmetrics(configparser.getServerList())

#def tmonStackMonitor():

if __name__== "main":
	file = open("tmon.log","w")
 	file.write(  str(tmonMetricsMonitor())  )
	file.close()
