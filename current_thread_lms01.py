#current_thread_lms01.py
connect("weblogic","passw0rd","t3://172.16.3.125:7001")
domainRuntime()
cd('ServerRuntimes')
cd('lms01')
cd("ThreadPoolRuntime/ThreadPoolRuntime")
threads = cmo.getExecuteThreads()
for thread in threads :
        isHogging = thread.isHogger()
        if isHogging > 0 :
         print "%s : %s " % (thread.getName(),thread.getCurrentRequest())
disconnect()
