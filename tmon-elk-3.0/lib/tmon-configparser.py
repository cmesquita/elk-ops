#jvm_metrics.py
import time as pytime
import ConfigParser, os


def configurationparser(): 
config = ConfigParser.ConfigParser()
config.readfp(open('tmon3.0.conf'))
config.read('tmon3.0.conf')

# get credentials
adminuser = config.get('weblogic_AdminConsole_credentials', 'username')
adminpass = config.get('weblogic_AdminConsole_credentials', 'password')

# get app name
appname = config.get('application','name')

# get server_containers
serverlist = config.get('weblogic_servers', 'server_list').split()

for i in serverlist:
	gcmethod=config.get('server_'+ i , 'gc_method')	
	if gcmethod !='g1' and gcmethod !='markSweep' and  gcmethod !="" :
		print "this is the current a value:" + gcmethod
		print "invalid gc method. please set g1 or markSweep"
	elif gcmethod == "" :
		gcmethod = 'g1'
		print "Using default gc method:" + a
return adminuser 
return adminpass
return appname
 
