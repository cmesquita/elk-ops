from wlstModule import *
import ..lib.tmon_threaddump as extract
def getThreadStucksCount( serverlist ):
        for i in serverlist:
                j = i.split()
                # [0] = container , [1] = method , [2] = user , [3] = pass , [4] = url
                connect(j[2],j[3],j[4])
		pwdstr = pwd()[:15]
		if pwdstr != 'serverRuntime:/':
			serverRuntime()
		cd('ThreadPoolRuntime/ThreadPoolRuntime' )
		threads = get('ExecuteThreads')
		for thread in threads :
        		isHogging = thread.isHogger()
        		if isHogging > 0 :
         			print "%s : %s " % (thread.getName(),thread.getCurrentRequest())
		disconnect()

#thread_dump_lms01.py
#connect("weblogic","passw0rd","t3://172.16.3.126:8001")
#threadDump()
#disconnect()

def getThreadStackHash( container, user , pass , url , thread_id):
	connect(user,pass,url)
	threadDump()
	file = 'Thread_Dump_'+container+'.txt'
	stacktrace = extract.extractStackTrace( file, thread_id )
	stackmd5 = hash.genMD5(stacktrace)
	elasticsearch.InsertIndex(stackmd5)
	disconnect()	




