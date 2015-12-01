#jvm_metrics.py
import time as pytime
import md5
import ConfigParser, os

user = "weblogic"
password = "manager1"
connect_string = "t3://192.168.47.205:7001"

# connecting weblogic	 
connect(user,password,connect_string)

def getStackHash():
	m=md5.new()
	m.update("test test")
	output = m.digest()
	hexoutput = m.hexdigest()
	print("digest= " + str(output))
	print("digest= " + str(hexoutput))	
	
if __name__== "main":
	getStackHash()
