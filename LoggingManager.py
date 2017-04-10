#-*- coding:utf-8 -*-
import logging
import types
from ssl import cert_time_to_seconds
from winerror import ERROR_INVALID_LOGON_HOURS
from cookielib import DAYS

# Define const variable for LOG Level.
# CRITICAL    50
# ERROR       40
# WARNING     30
# INFO        20
# DEBUG       10
# NOTSET      0  
CRITICAL=logging.CRITICAL
ERROR=logging.ERROR
WARNING=logging.WARNING
INFO=logging.INFO
DEBUG=logging.DEBUG
NOTSET=logging.NOTSET

lvlStrDict = {
    "CRITICAL":CRITICAL,
    "ERROR":ERROR,
    "WARNING":WARNING,
    "INFO":INFO,
    "DEBUG":DEBUG,
    "NOTSET":NOTSET
}

# logging output to streams such as sys.stdout, sys.stder
class StreamHandler:
    def __init__(self):
        # StreamHandler(stream=None)
        self.streamHnd = logging.StreamHandler()
        
    def getHandler(self):
        return self.streamHnd
    
    
# logging output to a disk file
class FileHandler:
    def __init__(self, file_path, mode='a'):
        # FileHandler(filename, mode='a', encoding=None, delay=False)
        # delay : then file opening is deferred until the first call to emit()
        self.fileHnd = logging.FileHandler(file_path, mode)
    
    def getHandler(self):
        return self.fileHnd
    
    
# supports rotation of disk log files at certain timed intervals.
# possible values is below. Note that they are not case sensitive.
# 'S' : Seconds
# 'M' : Minutes
# 'H' : Hours
# 'D' : Days
# 'W0' - 'W6' : Weekday(0=Monday)
# 'midnight' : Roll over at midnite
class TimeRotatingFileHandler:
    def __init__(self, file_path, when='h', interval=1):
        # TimedRotatingFileHandler(filename, when='h', interval=1, backupCount=0, encoding=None, delay=False, utc=False)
        # utc : times in UTC will be used
        # backupCount : If backupCount is nonzero, at most backupCount files will be kept
        # delay : then file opening is deferred until the first call to emit().
        self.timeRotatingFileHnd = logging.TimedRotationFileHandler(file_path, when, interval)
    
    def getHandler(self):
        return self.timeRotatingFileHnd
        
class LogHandler:
    def __init__(self, log_name):
        # set logger instance with the specified name
        self.logger = logging.getLogger(log_name)
        
        
        self.defaultFmt = '%(asctime)s|%(levelname)s:%(message)s'
        
        self.logLvl = logging.DEBUG
        self.logLevel(self.logLvl)
        self.handlerList = []
        
    def lvlStrToValue(self, lvlStr):
        if lvlStrDict.has_key(lvlStr):
            return lvlStrDict[lvlStr]
        else:
            return NOTSET
    
    def logLevel(self, lvl = None):
        if lvl == None:
            return self.logLvl
        else:
            if type(lvl) == types.StringType:
                lvl = lvl.upper()
                self.logLvl = self.lvlStrToValue(lvl)
            else:
                self.logLvl = lvl
            
            self.logger.setLevel(self.logLvl)
            
    # asctime     %(asctime)s     Human-readable time when the LogRecord was created. By default this is of the form ‘2003-07-08 16:49:45,896’ (the numbers after the comma are millisecond portion of the time).
    # created     %(created)f     Time when the LogRecord was created (as returned by time.time()).
    # filename    %(filename)s    Filename portion of pathname.
    # funcName    %(funcName)s    Name of function containing the logging call.
    # levelname   %(levelname)s   Text logging level for the message ('DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL').
    # levelno     %(levelno)s     Numeric logging level for the message (DEBUG, INFO, WARNING, ERROR, CRITICAL).
    # lineno      %(lineno)d      Source line number where the logging call was issued (if available).
    # module      %(module)s      Module (name portion of filename).
    # msecs       %(msecs)d       Millisecond portion of the time when the LogRecord was created.
    # message     %(message)s     The logged message, computed as msg % args. This is set when Formatter.format() is invoked.
    # name        %(name)s        Name of the logger used to log the call.
    # pathname    %(pathname)s    Full pathname of the source file where the logging call was issued (if available).
    # process     %(process)d     Process ID (if available).
    # processName %(processName)s Process name (if available).
    # thread      %(thread)d      Thread ID (if available).
    # threadName  %(threadName)s  Thread name (if available).        
    def getDefaultFormat(self):
        return self.defaultFmt
    
    def setFormat(self, fmt):
        self.defaultFmt = fmt
        tmpFormatter = self.logger.Formatter(fmt)
        fileHandler.setFormatter(formatter)
        streamHandler.setFormatter(formatter)

    def attachedFileHandler(self, file_path, mode='a', fmt=None):
        tmpFileHnd = FileHandler(file_path, mode).getHandler()
        
        if None == fmt:
            fmt = self.getDefaul+tFormat()
        
        tmpFileHnd.setFormatter(logging.Formatter(fmt))
        self.logger.addHandler(tmpFileHnd)
            
    def attachedStreamHandler(self, fmt=None):
        tmpStreamHnd = StreamHandler().getHandler()
        
        if None == fmt:
            fmt = self.getDefaultFormat()
        
        tmpStreamHnd.setFormatter(logging.Formatter(fmt))
        self.logger.addHandler(tmpStreamHnd)
    
    # Removes the specified handler hdlr from this logger.
    def removeHandler(self, hdlr):
        self.logger.removeHandler
        
    # Logs a message with level DEBUG on this logge
    # mesg : the message format string
    # args : arguments which are merged into msg using the string formatting operator
    def debugMesg(self, mesg, *args):
        self.logger.debug(mesg, *args)
    
    # Logs a message with level WARNING on this logger.
    # mesg : the message format string
    # args : arguments which are merged into msg using the string formatting operator
    def warnMesg(self, mesg, *args):
        self.logger.warning(mesg, *args)
    
    # Logs a message with level CRITICAL on this logger.
    # mesg : the message format string
    # args : arguments which are merged into msg using the string formatting operator
    def criticalMesg(self, mesg, *args):
        self.logger.critical(mesg, *args)
        
    # Logs a message with level ERROR on this logger.
    # mesg : the message format string
    # args : arguments which are merged into msg using the string formatting operator
    def errorMesg(self, mesg, *args):
        self.logger.error(mesg, *args)
        
    # Logs a message with level INFO on this logger.
    # mesg : the message format string
    # args : arguments which are merged into msg using the string formatting operator
    def infoMesg(self, mesg, *args):
        self.logger.info(mesg, *args)
        
    # Logs a message with integer level lvl on this logger.
    # mesg : the message format string
    # args : arguments which are merged into msg using the string formatting operator
    def logMesg(self, lvl, mesg, *args):
        self.logger.log(lvl, mesg, *args)
        
if __name__ == "__main__":
    print "Program test"
    logMng = LogHandler("Test")
    logMng.logLevel("CRITICAL")
    print logMng.logLevel()
    logMng.attachedStreamHandler()
    
    logMng.debugMesg("Test Message")
    logMng.debugMesg("Test Message(%d)", 5)