#thread_dump.sh
JAVA_HOME=/u01/Middleware/jdk1.7.0_51
$JAVA_HOME/bin/java -cp /u01/Middleware/Oracle_Home/wlserver/server/lib/weblogic.jar weblogic.WLST $1
