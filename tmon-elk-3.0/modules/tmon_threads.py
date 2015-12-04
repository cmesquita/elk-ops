from wlstModule import *
import lib.tmon_threaddump as extract
import lib.tmon_md5	as hash
import lib.tmon_elasticsearch as elasticsearch

def getThreadStucksCount( serverlist ):
	threads_details = []
	thread_hogging = []
        for i in serverlist:
                j = i.split()
                # [0] = container , [1] = method , [2] = user , [3] = pass , [4] = url , [5] = appName
                connect(j[2],j[3],j[4])
		pwdstr = pwd()[:15]
		if pwdstr != 'serverRuntime:/':
			serverRuntime()
		cd('ThreadPoolRuntime/ThreadPoolRuntime' )
		threads = get('ExecuteThreads')
		hogging_count =  get('HoggingThreadCount')
		stuck_count = get('StuckThreadCount')
		for thread in threads :
        		isHogging = thread.isHogger()
        		if isHogging == 0 :
				thread_info = thread.getName().split()
				thread_hogging.append(thread_info[1] + ' ' + thread_info[2])
         			#print "%s : %s " % (thread.getName(),thread.getCurrentRequest())
		#[0] threads id list , [1] count threads hogging , [2] count threads stuck 
		threads_details.append(thread_hogging)
		threads_details.append(hogging_count)
		threads_details.append(stuck_count)  
		return threads_details
		disconnect()

def getThreadStackHash( serverlist , thread_id):
	for i in serverlist:
		j = i.split()
		# [0] = container , [1] = method , [2] = user , [3] = pass , [4] = url , [5] = appName
		connect(j[2],j[3],j[4])
		threadDump()
		file = 'Thread_Dump_'+j[0]+'.txt'
		stacktrace = extract.extractStackTrace( file, thread_id )
		stackmd5 = hash.genMD5(stacktrace)
		elasticsearch.InsertIndex(stackmd5)
		return stackmd5
		disconnect()	
