#from teste.tmon_confgparser import *
import  lib.tmon_configparser as configparser
import  modules.tmon_metrics as metrics


#print configparser.getHoggingThread()
#print  metrics.getGCmetrics()

for i in configparser.getServerList():
	print i
