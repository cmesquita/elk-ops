#jvm_metrics.py
import time as pytime
import ConfigParser, os


config = ConfigParser.ConfigParser()
config.readfp(open('tmon3.0.conf'))
config.read('tmon3.0.conf')
#
# weblogic admin console credentials
#
def getAdminUser():
        adminuser = config.get('weblogic_AdminConsole_credentials', 'username')
	return adminuser

def getAdminPass():
        adminpass = config.get('weblogic_AdminConsole_credentials', 'password')
	return adminpass

def getConnectString():
	adminpass = config.get('weblogic_AdminConsole_credentials', 'connect_string')
	return adminpass

#
# application name
#

def getAppName():
	appname = config.get('application','name')
	return appname

#
# weblogic server list and its gc methods
#

def getServerList():
	gcmethod = []
	serverlist = config.get('weblogic_servers', 'server_list').split()
	for i in serverlist:
		gcserverlist = i + ' ' + config.get('server_'+ i , 'gc_method') + ' ' + config.get('server_'+ i , 'username') + ' ' + config.get('server_'+ i , 'password') + ' ' + config.get('server_'+ i , 'connect_string') + ' ' + config.get('server_'+ i , 'app_name')
		gcmethod.append(gcserverlist)
		'''
		if gcmethod[len(gcmethod)-1] !='g1' and gcmethod[len(gcmethod)-1] !='markSweep' and  gcmethod[len(gcmethod)-1] !="" :
			print "this is the current garbage collector value:" + str(gcmethod[len(gcmethod)-1])
			print "invalid gc method. please set g1 or markSweep"
		elif gcmethod[len(gcmethod)-1] == "" :
			gcmethod.append('g1')
			print "Using default gc method:" +  str(gcmethod[len(gcmethod)-1])
		'''
	return gcmethod

#
# hogging thread thresholds
#

def getHoggingThread():
	thread_duration = config.get('hogging_thread','thread_duration')
	return thread_duration

#
# get elasticsearch url
#
def getElasticsearch():
	el_url = config.get('elasticsearch','url')
	return el_url
