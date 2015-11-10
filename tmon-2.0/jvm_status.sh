#jvm_status.sh
$JAVA_HOME/bin/java -cp /u01/Middleware/Oracle_Home/wlserver/server/lib/weblogic.jar weblogic.WLST status_$1.py |egrep -ir "OpenSocket|OpenSession|getHoggingThreadCount|getStuckThreadCount"
