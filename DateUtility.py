#!/usr/bin/python
# -*- coding: euc-kr -*-

'''
%a Locale��s abbreviated weekday name.   
%A Locale��s full weekday name.   
%b Locale��s abbreviated month name.   
%B Locale��s full month name.   
%c Locale��s appropriate date and time representation.   
%d Day of the month as a decimal number [01,31].   
%f Microsecond as a decimal number [0,999999], zero-padded on the left (1) 
%H Hour (24-hour clock) as a decimal number [00,23].   
%I Hour (12-hour clock) as a decimal number [01,12].   
%j Day of the year as a decimal number [001,366].   
%m Month as a decimal number [01,12].   
%M Minute as a decimal number [00,59].   
%p Locale��s equivalent of either AM or PM. (2) 
%S Second as a decimal number [00,61]. (3) 
%U Week number of the year (Sunday as the first day of the week) as a decimal number [00,53]. All days in a new year preceding the first Sunday are considered to be in week 0. (4) 
%w Weekday as a decimal number [0(Sunday),6].   
%W Week number of the year (Monday as the first day of the week) as a decimal number [00,53]. All days in a new year preceding the first Monday are considered to be in week 0. (4) 
%x Locale��s appropriate date representation.   
%X Locale��s appropriate time representation.   
%y Year without century as a decimal number [00,99].   
%Y Year with century as a decimal number.   
%z UTC offset in the form +HHMM or -HHMM (empty string if the the object is naive). (5) 
%Z Time zone name (empty string if the object is naive).   
%% A literal '%' character. 
'''
import types
import locale

# A datetime object is a single object containing all the information from a date object and a time object.
import datetime


abbreveWeekdayNameDict = {
        "Mon" : u"��",
        "Tue" : u"ȭ",
        "Wed" : u"��",
        "Thu" : u"��",
        "Fri" : u"��",
        "Sat" : u"��",
        "Sun" : u"��"
}

WeekdayNameDict = {
        "Monday" : u"������",
        "Tuesday" : u"ȭ����",
        "Wednesday" : u"������",
        "Thursday" : u"�����",
        "Friday" : u"�ݿ���",
        "Saturday" : u"�����",
        "Sunday" : u"�Ͽ���"
}

# Return current date object
def getDateObj():
    return datetime.date

# A date object represents a date (year, month and day) in an idealized calendar
def getDateObjWithArg(year, month, day):
    return datetime.date(year, month, day)

# ���ڿ��� ���ڵ���(�ַ� �����ڵ带 Ÿ�ڵ�� �����)
def getLocaleEncoding(sourceStr):    
    return sourceStr.encode(locale.getpreferredencoding())

# ���ڿ��� ���ڵ���(�ַ� Ÿ�ڵ带 �����ڵ�� �����)
def getLocaleDecoding(sourceStr):    
    return sourceStr.decode(locale.getpreferredencoding())
    
# ���ó�¥�� �ش��ϴ� ��ü ��ȯ
# Return the current local datetime, with tzinfo None.
def getTodayDateObject():
    return datetime.datetime.today()

    
# ���ó�¥�� �ش��ϴ� ��ü ��ȯ(Time Zone ��������)
# Return the current local date and time
def getNowDateTimeObject(tz = None):
    return datetime.datetime.now(tz)

# �Ķ������ ������ datetime ��ü ����(int���� �Ķ���ͷ� �����ؾ���)
# datetime.datetime(year, month, day[, hour[, minute[, second[, microsecond[, tzinfo]]]]]) 
def makeDateTimeObject(year, month, day, hour=0, minute=0, second=0, microsecond=0):    
    return datetime.datetime(year, month, day, hour, minute, second, microsecond)

########################################
# A timedelta object represents a duration, the difference between two dates or times.
# datetime.timedelta([days[, seconds[, microseconds[, milliseconds[, minutes[, hours[, weeks]]]]]]]) 

def getMonthsDeltaFromBaseDate(baseDate, monthsDelta):
    deltaMonthObj = makeDateTimeObject(baseDate.year, baseDate.month + monthsDelta, baseDate.day, 
                                       baseDate.hour, baseDate.minute, baseDate.second, baseDate.microsecond)
    return deltaMonthObj

# �����Ͽ��� ������ ������ ����/���� ��¥ ������Ʈ�� ��ȯ��
def getWeeksDeltaFromBaseDate(baseDate, weeksDelta):
    return baseDate + datetime.timedelta(weeks = weeksDelta)

# �����Ͽ��� �Ϸ� ������ ����/���� ��¥ ������Ʈ�� ��ȯ��
def getDaysDeltaFromBaseDate(baseDate, daysDelta):
    return baseDate + datetime.timedelta(days = daysDelta)

# ���ؽð����� �ð� ������ ����/���� �ð� ������Ʈ�� ��ȯ��.
def getHoursDeltaFromBaseDate(baseDate, hoursDelta):
    return baseDate + datetime.timedelta(hours=hoursDelta)

# ���ؽð����� �� ������ ����/���� �ð� ������Ʈ�� ��ȯ��.
def getMinutesDeltaFromBaseDate(baseDate, minutesDelta):
    return baseDate + datetime.timedelta(minutes=minutesDelta)


# ������ �������� ������ ������ ����/���� ��¥ ������Ʈ�� ��ȯ��
def getWeeksDeltaFromNow(weeksDelta):
    return getWeeksDeltaFromBaseDate(getTodayDateObject(), weeksDelta)

# ������ �������� �Ϸ� ������ ����/���� ��¥ ������Ʈ�� ��ȯ��
def getDaysDeltaFromNow(daysDelta):
    return getDaysDeltaFromBaseDate(getTodayDateObject(), daysDelta)

# ����ð����� �ð� ������ ����/���� �ð� ������Ʈ�� ��ȯ��.
def getHoursDeltaFromNow(hoursDelta):
    return getHoursDeltaFromBaseDate(getTodayDateObject(), hoursDelta)

# ����ð����� �� ������ ����/���� �ð� ������Ʈ�� ��ȯ��.
def getMinutesDeltaFromNow(minutesDelta):
    return getMinutesDeltaFromBaseDate(getTodayDateObject(), minutesDelta)

# Ư�� datetime ��ü�� ���ڿ��� ������ ���˿� ���� ��ȯ��
def getDateTimeStr(dateObj, fmt):
    # �����ڵ� ���� Ȯ���� ���ڵ� ����
    unicodeFlag = False
    if  type(fmt) == types.UnicodeType:
        unicodeFlag = True
    
    # �����ڵ� Ÿ���� ���ڿ��� ��� ���ڵ���
    if unicodeFlag == True:
        fmt = getLocaleEncoding(fmt)
    
    dateTimeStr = dateObj.strftime(fmt)
    
    # ���� ����� �ٽ� �����ڵ�� ���ڵ��Ѵ�
    if unicodeFlag == True:
        dateTimeStr = getLocaleDecoding(dateTimeStr)
    
    return dateTimeStr

# Ư�� datetime ��ü�� ���ڿ��� 0�� �����ϰ� ��ȯ��
def getDateTimeStrWithoutZP(dateObj, fmt):
    datetimeStr = getDateTimeStr(dateObj, fmt)
    if dateObj.month < 10 :
        datetimeStr = datetimeStr.replace("%02d" % dateObj.month, "%d" % dateObj.month)
        
    if dateObj.day < 10 :
        datetimeStr = datetimeStr.replace("%02d" % dateObj.day, "%d" % dateObj.day)
    
    return datetimeStr

# ���ϰ��� �ܾ�(��~��)�� ����� �ѱ۷� �����Ͽ� ��ȯ��
def getDateTimeStrWithKorWeekdayName(dateObj, fmt): 
    datetimeStr = getDateTimeStr(dateObj, fmt)
    
    # ������ ������ ~ �Ͽ��� �ΰ��
    fullDayNameKeys = WeekdayNameDict.keys()
    for key in fullDayNameKeys:
        if key in datetimeStr:
            datetimeStr = datetimeStr.replace(key, WeekdayNameDict[key])
    
    # ������ �� ~ �� �ΰ��
    abbreveDayNameKeys = abbreveWeekdayNameDict.keys()
    for key in abbreveDayNameKeys:
        if key in datetimeStr:
            datetimeStr = datetimeStr.replace(key, WeekdayNameDict[key])
    
    return datetimeStr
            
# ���� ��¥�� ���ڿ��� ������ ���˿� ���� ��ȯ��
def getTodayStr(fmt):
    return getDateTimeStr(getTodayDateObject(), fmt)

# ���� ��¥�� ���ڿ��� 0�� �����ϰ� ��ȯ��
def getTodayStrWithoutZP(fmt):
    return getDateTimeStrWithoutZP(getTodayDateObject(), fmt)


def getTodayStrWithWeekNumberOfMonth(dateFmt, fullStrFmt):
        todayDataStr = getTodayStr(dateFmt)
        return fullStrFmt % (todayDataStr, getWeekNumberOfMonth())
        

# datetime ��ü�� �������� �Ǵ��� �������� ���� ��� ���� ��¥�� ��ü�� �����Ͽ� ��ȯ
def checkDateObject(dateObject):
    if dateObject == None:
        dateObject = getTodayDateObject()
    
    return dateObject

# Monday is 0 and Sunday is 6
def getWeekDay(dateObject = None):
    dateObject = checkDateObject(dateObject)
    return dateObject.weekday()

# Monday is 1 and Sunday is 7'
def getIsoWeekDay(dateObject = None):
    dateObject = checkDateObject(dateObject)
    return dateObject.isoweekday()

# Return a 3-tuple, (ISO year, ISO week number, ISO weekday). 
def getIsoCalendar(dateObject = None):
    dateObject = checkDateObject(dateObject)
    return dateObject.isocalendar()

# �ش� ���� ������ ��, �ָ� Ʃ�����·� ��ȯ��
def getLastDayInfoOfMonth(dateObject = None):
    dateObject = checkDateObject(dateObject)
    nextMonth = getDateObjWithArg(dateObject.year, dateObject.month + 1, 1)
    lastDayDate = getDaysDeltaFromBaseDate(nextMonth, -1)

    return (lastDayDate.isocalendar()[2], lastDayDate.day)

# �ش� ���� ù��° ���� ��ȯ��
def getFirstDayOfWeek(dateObject = None):
    dateObject = checkDateObject(dateObject)
    daysDelta = getWeekDay(dateObject) * -1
    dateObject = getDaysDeltaFromBaseDate(dateObject, daysDelta) 
    
    return dateObject.day

# �ش� ���� ������ ���� ��ȯ��
def getLastDayOfWeek(dateObject = None):
    dateObject = checkDateObject(dateObject)
    daysDelta = 6 - getWeekDay(dateObject)
    dateObject = getDaysDeltaFromBaseDate(dateObject, daysDelta)
    
    return dateObject.day

# ������ �����ϰ� �ݿ��Ͽ� �ش��ϴ� ���� Ʃ�÷� ��ȯ��
def getWorkingDay(dateObject = None):
    dateObject = checkDateObject(dateObject)
    startDay = getFirstDayOfWeek(dateObject)
    
    return (startDay, startDay+4)

# �ش� �޿��� ���° ������ ã�Ƽ� ��ȯ�ϴ� �Լ�
def getWeekNumberOfMonth(dateObject = None):
    dateObject = checkDateObject(dateObject)
        
    firstDayOfMonthObj = dateObject.replace(day=1)
    weekNumOfMonth = (dateObject.isocalendar()[1] - firstDayOfMonthObj.isocalendar()[1]) + 1
    
    return weekNumOfMonth

# ������ ù��°�� ���θ� ��ȯ��
def isFirstWeekOfMonth():
    firstWeekFlag = False
    if getWeekNumberOfMonth() == 1:
        firstWeekFlag = True
    
    return firstWeekFlag

# ������ �������� ���θ� ��ȯ��
def isLastWeekOfMonth():
    lastDayInfoTuple = getLastDayInfoOfMonth()
    currentWeekNumber = getWeekNumberOfMonth()
    
    lastWeekFlag = False
    if lastDayInfoTuple[0] == currentWeekNumber:
        lastWeekFlag = True
    
    return lastWeekFlag
    


if __name__ == "__main__" :
    nowObj = getNowDateTimeObject()
    userObj = makeDateTimeObject(nowObj.year, nowObj.month, nowObj.day, nowObj.hour, nowObj.minute)
    print userObj

    print getLastDayInfoOfMonth()
    print getFirstDayOfWeek()
    print getLastDayOfWeek()
    print getWorkingDay()