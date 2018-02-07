#!/usr/bin/env python2.7
import glob, os, datetime

allLogsGlobTime = "03:01"

log_dir = "/path/to/logs/"
log_dir_alt1 = "/path/to/logs2/"
log_dir_alt1 = "/path/to/logs3/"

# Use Globs to pull list of logs to monitor
# Only once a day, pull all the logs.
# Otherwise, pull just the current log (ie. ".log")
if datetime.datetime.strftime(datetime.datetime.now(), "%H:%M") in allLogsGlobTime:
    logs = glob.glob(log_dir + '*.log.*')
    logs.extend(glob.glob(log_dir + '*/*.log.*'))
else:
    logs = glob.glob(log_dir + '*.log')
    logs.extend(glob.glob(log_dir_alt1 + '*.rest'))
    logs.extend(glob.glob(log_dir_alt2 + '*/*.log'))
    

# Loop through all the logs in the list and write file stats for each to monitorlog
timestamp = datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%dT%H:%M:%S")
for log in logs:
    s = os.stat(log)
    logChmod = oct(s.st_mode & 0777)[1:]
    print('%s log_name=%s, log_chmod=%s, log_ctime=%s, log_mtime=%s, log_size=%s' % (timestamp, log, logChmod, s.st_atime, s.st_mtime, s.st_size))
