# elk-ops
## logstash
Logstash artifacts related to filters and plugins required to managed (apache, weblogic, weblogic http connector ) ELK requirements.

## logstash-forwarder 
Logstash agent to forwarder weblogic and apache log files 

## tmon-2.0
Weblogic scripting tool to get many JVM metrics related. 

## tmon-elk-3.0
Weblogic scripting tool to creates log files to be processed by ELK platform. 
### example usage of jvm_metrics.py
[oracle@weblogic elk-ops]$ . /u01/app/Oracle/Middleware/Oracle_Home/wlserver/server/bin/setWLSEnv.sh
oracle@weblogic elk-ops]$ java weblogic.WLST tmon-elk-3.0/jvm_metrics.py
