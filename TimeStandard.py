#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/11/15 11:06 下午
# @Author : gaofujie
# @File : TimeStandard.py
# @namespace scheme: MyFile, MyClass, myFunc, my_vaR, CONST
# @var name type: classC, dictD, listL, stringS, intI, floatF, tupleT


# imports
import datetime

## time
class TimeStandard():
    # datetime.datetime type has year, day, ... METHODS (not properties)
    # we transform timestamp/timestring to datetime.datetime type for different timezone
    # import time, datetime
    def __init__(self):
        self.clear()
    def clear(self):
        self.date_timeC = None
        self.week_of_yearI = None
        self.day_of_weekI = None
        self.quarter_of_dayI = None
    def update(self):
        self.week_of_yearI = self.date_timeC.isocalendar()[1]
        self.day_of_weekI = self.date_timeC.weekday()
        self.quarter_of_dayI = self.date_timeC.hour * 4 + self.date_timeC.minute//15
    def hourOffset(self, timezoneS):
        return 0 if (timezoneS=='UTC') else int(timezoneS[3:])
    def processTimestamp(self, timestampF, timezone_inS='UTC+8', timezone_outS='UTC+8'):
        # fromtimestamp: default out UTC+8 (similar to time.localtime())
        self.clear()
        delta_hourI = self.hourOffset(timezone_outS) - self.hourOffset(timezone_inS)
        self.date_timeC = datetime.datetime.fromtimestamp(timestampF) \
                          + datetime.timedelta(hours=delta_hourI)
        self.update()
    def processTimeString(self, timeS, time_schemeS='%Y-%m-%d %H:%M:%S',
                          timezone_inS = 'UTC+8', timezone_outS = 'UTC+8'):
        # strptime: default out UTC+8 (similar to time.localtime())
        self.clear()
        delta_hourI = self.hourOffset(timezone_outS) - self.hourOffset(timezone_inS)
        self.date_timeC = datetime.datetime.strptime(timeS, time_schemeS) \
                          + datetime.timedelta(hours = delta_hourI)
        self.update()

if __name__ == '__main__':
    ts = TimeStandard()
    import time
    ts.processTimestamp(time.time())
    print(ts.date_timeC)
    print(ts.day_of_weekI, ts.week_of_yearI, ts.quarter_of_dayI)