#from teste.tmon_confgparser import *
import  lib.tmon_configparser as configparser

print configparser.getHoggingThread()

for i in configparser.getServerList():
	print i
