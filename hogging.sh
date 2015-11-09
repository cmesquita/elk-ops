#hogging.sh
JAVA_HOME=/u01/Middleware/jdk1.7.0_51
$JAVA_HOME/bin/java -cp /u01/Middleware/Oracle_Home/wlserver/server/lib/weblogic.jar weblogic.WLST /home/oracle/ilegra/tmon-2.0/current_thread_$1.py |grep -ir ExecuteThread|awk '{print $2" "$3" "$17}'
