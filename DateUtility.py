#!/usr/bin/python
# -*- coding: euc-kr -*-

'''
%a Locale’s abbreviated weekday name.   
%A Locale’s full weekday name.   
%b Locale’s abbreviated month name.   
%B Locale’s full month name.   
%c Locale’s appropriate date and time representation.   
%d Day of the month as a decimal number [01,31].   
%f Microsecond as a decimal number [0,999999], zero-padded on the left (1) 
%H Hour (24-hour clock) as a decimal number [00,23].   
%I Hour (12-hour clock) as a decimal number [01,12].   
%j Day of the year as a decimal number [001,366].   
%m Month as a decimal number [01,12].   
%M Minute as a decimal number [00,59].   
%p Locale’s equivalent of either AM or PM. (2) 
%S Second as a decimal number [00,61]. (3) 
%U Week number of the year (Sunday as the first day of the week) as a decimal number [00,53]. All days in a new year preceding the first Sunday are considered to be in week 0. (4) 
%w Weekday as a decimal number [0(Sunday),6].   
%W Week number of the year (Monday as the first day of the week) as a decimal number [00,53]. All days in a new year preceding the first Monday are considered to be in week 0. (4) 
%x Locale’s appropriate date representation.   
%X Locale’s appropriate time representation.   
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
        "Mon" : u"월",
        "Tue" : u"화",
        "Wed" : u"수",
        "Thu" : u"목",
        "Fri" : u"금",
        "Sat" : u"토",
        "Sun" : u"일"
}

WeekdayNameDict = {
        "Monday" : u"월요일",
        "Tuesday" : u"화요일",
        "Wednesday" : u"수요일",
        "Thursday" : u"목요일",
        "Friday" : u"금요일",
        "Saturday" : u"토요일",
        "Sunday" : u"일요일"
}

# Return current date object
def getDateObj():
    return datetime.date

# A date object represents a date (year, month and day) in an idealized calendar
def getDateObjWithArg(year, month, day):
    return datetime.date(year, month, day)

# 문자열을 인코딩함(주로 유니코드를 타코드로 변경시)
def getLocaleEncoding(sourceStr):    
    return sourceStr.encode(locale.getpreferredencoding())

# 문자열을 디코딩함(주로 타코드를 유니코드로 변경시)
def getLocaleDecoding(sourceStr):    
    return sourceStr.decode(locale.getpreferredencoding())
    
# 오늘날짜에 해당하는 객체 반환
# Return the current local datetime, with tzinfo None.
def getTodayDateObject():
    return datetime.datetime.today()

    
# 오늘날짜에 해당하는 객체 반환(Time Zone 설정가능)
# Return the current local date and time
def getNowDateTimeObject(tz = None):
    return datetime.datetime.now(tz)

# 파라미터의 값으로 datetime 객체 생성(int값을 파라미터로 전달해야함)
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

# 기준일에서 일주일 단위로 이전/이후 날짜 오브젝트를 반환함
def getWeeksDeltaFromBaseDate(baseDate, weeksDelta):
    return baseDate + datetime.timedelta(weeks = weeksDelta)

# 기준일에서 하루 단위로 이전/이후 날짜 오브젝트를 반환함
def getDaysDeltaFromBaseDate(baseDate, daysDelta):
    return baseDate + datetime.timedelta(days = daysDelta)

# 기준시간에서 시간 단위로 이전/이후 시간 오브젝트를 반환함.
def getHoursDeltaFromBaseDate(baseDate, hoursDelta):
    return baseDate + datetime.timedelta(hours=hoursDelta)

# 기준시간에서 분 단위로 이전/이후 시간 오브젝트를 반환함.
def getMinutesDeltaFromBaseDate(baseDate, minutesDelta):
    return baseDate + datetime.timedelta(minutes=minutesDelta)


# 당일을 기준으로 일주일 단위로 이전/이후 날짜 오브젝트를 반환함
def getWeeksDeltaFromNow(weeksDelta):
    return getWeeksDeltaFromBaseDate(getTodayDateObject(), weeksDelta)

# 당일을 기준으로 하루 단위로 이전/이후 날짜 오브젝트를 반환함
def getDaysDeltaFromNow(daysDelta):
    return getDaysDeltaFromBaseDate(getTodayDateObject(), daysDelta)

# 현재시간에서 시간 단위로 이전/이후 시간 오브젝트를 반환함.
def getHoursDeltaFromNow(hoursDelta):
    return getHoursDeltaFromBaseDate(getTodayDateObject(), hoursDelta)

# 현재시간에서 분 단위로 이전/이후 시간 오브젝트를 반환함.
def getMinutesDeltaFromNow(minutesDelta):
    return getMinutesDeltaFromBaseDate(getTodayDateObject(), minutesDelta)

# 특정 datetime 객체의 문자열을 정해진 포맷에 따라 반환함
def getDateTimeStr(dateObj, fmt):
    # 유니코드 여부 확인후 인코딩 수행
    unicodeFlag = False
    if  type(fmt) == types.UnicodeType:
        unicodeFlag = True
    
    # 유니코드 타입의 문자열인 경우 인코딩함
    if unicodeFlag == True:
        fmt = getLocaleEncoding(fmt)
    
    dateTimeStr = dateObj.strftime(fmt)
    
    # 최종 결과를 다시 유니코드로 디코드한다
    if unicodeFlag == True:
        dateTimeStr = getLocaleDecoding(dateTimeStr)
    
    return dateTimeStr

# 특정 datetime 객체의 문자열을 0를 제외하고 반환함
def getDateTimeStrWithoutZP(dateObj, fmt):
    datetimeStr = getDateTimeStr(dateObj, fmt)
    if dateObj.month < 10 :
        datetimeStr = datetimeStr.replace("%02d" % dateObj.month, "%d" % dateObj.month)
        
    if dateObj.day < 10 :
        datetimeStr = datetimeStr.replace("%02d" % dateObj.day, "%d" % dateObj.day)
    
    return datetimeStr

# 요일관련 단어(월~금)를 영어에서 한글로 변경하여 반환함
def getDateTimeStrWithKorWeekdayName(dateObj, fmt): 
    datetimeStr = getDateTimeStr(dateObj, fmt)
    
    # 요일이 월요일 ~ 일요일 인경우
    fullDayNameKeys = WeekdayNameDict.keys()
    for key in fullDayNameKeys:
        if key in datetimeStr:
            datetimeStr = datetimeStr.replace(key, WeekdayNameDict[key])
    
    # 요일이 월 ~ 금 인경우
    abbreveDayNameKeys = abbreveWeekdayNameDict.keys()
    for key in abbreveDayNameKeys:
        if key in datetimeStr:
            datetimeStr = datetimeStr.replace(key, WeekdayNameDict[key])
    
    return datetimeStr
            
# 오늘 날짜의 문자열을 정해진 포맷에 따라 반환함
def getTodayStr(fmt):
    return getDateTimeStr(getTodayDateObject(), fmt)

# 오늘 날짜의 문자열을 0를 제외하고 반환함
def getTodayStrWithoutZP(fmt):
    return getDateTimeStrWithoutZP(getTodayDateObject(), fmt)


def getTodayStrWithWeekNumberOfMonth(dateFmt, fullStrFmt):
        todayDataStr = getTodayStr(dateFmt)
        return fullStrFmt % (todayDataStr, getWeekNumberOfMonth())
        

# datetime 객체의 생성여부 판단후 생성되지 않은 경우 오늘 날짜의 객체를 생성하여 반환
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

# 해당 달의 마지막 일, 주를 튜플형태로 반환함
def getLastDayInfoOfMonth(dateObject = None):
    dateObject = checkDateObject(dateObject)
    nextMonth = getDateObjWithArg(dateObject.year, dateObject.month + 1, 1)
    lastDayDate = getDaysDeltaFromBaseDate(nextMonth, -1)

    return (lastDayDate.isocalendar()[2], lastDayDate.day)

# 해당 주의 첫번째 일을 반환함
def getFirstDayOfWeek(dateObject = None):
    dateObject = checkDateObject(dateObject)
    daysDelta = getWeekDay(dateObject) * -1
    dateObject = getDaysDeltaFromBaseDate(dateObject, daysDelta) 
    
    return dateObject.day

# 해당 주의 마지막 일을 반환함
def getLastDayOfWeek(dateObject = None):
    dateObject = checkDateObject(dateObject)
    daysDelta = 6 - getWeekDay(dateObject)
    dateObject = getDaysDeltaFromBaseDate(dateObject, daysDelta)
    
    return dateObject.day

# 한주의 월요일과 금요일에 해당하는 일을 튜플로 반환함
def getWorkingDay(dateObject = None):
    dateObject = checkDateObject(dateObject)
    startDay = getFirstDayOfWeek(dateObject)
    
    return (startDay, startDay+4)

# 해당 달에서 몇번째 주인지 찾아서 반환하는 함수
def getWeekNumberOfMonth(dateObject = None):
    dateObject = checkDateObject(dateObject)
        
    firstDayOfMonthObj = dateObject.replace(day=1)
    weekNumOfMonth = (dateObject.isocalendar()[1] - firstDayOfMonthObj.isocalendar()[1]) + 1
    
    return weekNumOfMonth

# 오늘이 첫번째주 여부를 반환함
def isFirstWeekOfMonth():
    firstWeekFlag = False
    if getWeekNumberOfMonth() == 1:
        firstWeekFlag = True
    
    return firstWeekFlag

# 오늘이 마지막주 여부를 반환함
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