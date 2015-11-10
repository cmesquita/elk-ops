#tmon-2.0.sh
#function: script to find out hogging threads and extract its stack trace.
#author: cesar mesquita (cesar.mesquita@ilegra.com)
#date: 18/08/2014

. /home/oracle/.bash_profile

JAVA_HOME=/u01/Middleware/jdk1.7.0_51

HOGGING_CHECK_CONF=/home/oracle/ilegra/tmon-2.0/container_list.conf
HOGGING_CHECK_OUTPUT=/home/oracle/ilegra/tmon-2.0/logs/tmon_`date +"%H%M%S-%m_%d_%y"`.log
HOGGING_LOCK_FILE=/home/oracle/ilegra/tmon-2.0/tmon20.lck
HOGGING_EXEC_TIME=`date +"%m-%d-%y %H:%M:%S"`
HOGGING_THREADS_DURATION=300000

if [ -f $HOGGING_LOCK_FILE ]; then

 echo "It seems that tmon 2.0 is already running please check for tmon-2.0.sh process running."
 echo "In case of no process alive, please remove $HOGGING_LOCK_FILE to run tmon again."

else
 #creating tmon lock file to prevent duplicated process.
 touch $HOGGING_LOCK_FILE
 echo "TMON-2.0 execution time at $HOGGING_EXEC_TIME"
 echo "Please check $HOGGING_CHECK_OUTPUT for hogging threads reference."
 cat $HOGGING_CHECK_CONF | while read line1
 do
  #create a list of hogging threads
  echo " "
  echo "#### $line1 ####"
  echo "#### $line1 ####"  >> $HOGGING_CHECK_OUTPUT
  /home/oracle/ilegra/tmon-2.0/jvm_status.sh $line1
  /home/oracle/ilegra/tmon-2.0/hogging.sh $line1|awk '{print $2" "$3}' |  sed "s/'//g" > /tmp/hogging_aux.txt
  #if hogging threads exists, a thread dump must be done.
  if [ `cat /tmp/hogging_aux.txt |wc -l` -gt 0  ]; then

   /home/oracle/ilegra/tmon-2.0/thread_dump.sh thread_dump_$line1.py >> /dev/null
   TDUMP=/home/oracle/ilegra/tmon-2.0/Thread_Dump_$line1.txt

   #looping hogging threads, stack trace and execution time

   cat /tmp/hogging_aux.txt | while read line
   do
     thread_id=`echo $line | awk '{print $1}'`
     thread_duration=`echo $line | awk '{print $2}'`
     if [ $thread_duration -gt $HOGGING_THREADS_DURATION ]; then
       echo "thread id:: $thread_id is running about $thread_duration (ms)." >> $HOGGING_CHECK_OUTPUT
       echo "Extracting thread dump from thread id:: $thread_id" >> $HOGGING_CHECK_OUTPUT
       sed '/'ExecuteThread:" "\'$thread_id\''/,/^$/!d' $TDUMP >> $HOGGING_CHECK_OUTPUT
     else
       echo "thread id:: $thread_id is running about $thread_duration (ms)." >> $HOGGING_CHECK_OUTPUT
       echo "no actions is required once $thread_duration is not greater than $HOGGING_THREADS_DURATION(ms)." >> $HOGGING_CHECK_OUTPUT
     fi
   done
   echo " " >> $HOGGING_CHECK_OUTPUT
  else

   echo "there is no hogging threads at `date +"%m-%d-%y %H:%M:%S"`." >> $HOGGING_CHECK_OUTPUT
   echo " "  >> $HOGGING_CHECK_OUTPUT

  fi
 done
 echo "End Execution at $HOGGING_EXEC_TIME." >> $HOGGING_CHECK_OUTPUT
 echo "----------------------------" >> $HOGGING_CHECK_OUTPUT
 echo " " >> $HOGGING_CHECK_OUTPUT

 rm $HOGGING_LOCK_FILE
fi

