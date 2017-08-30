##Python内建模块 datetime 练习：
##假设你获取了用户输入的日期和时间如2015-1-21 9:01:30，以及一个时区信息如UTC+5:00，均是str，请编写一个函数将其转换为timestamp：
import re
from datetime import datetime, timezone, timedelta
def to_timestamp(dt_str, tz_str):
    dt=datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    utc = re.match(r'^UTC([+|-])([0-9]{1,2})\:(\d{2})$', tz_str) ##用正则表达式识别时区信息

    if utc: ##附加时区信息
        if utc.group(1) == '+':
            cur_dt = dt.replace(tzinfo=timezone(timedelta(hours=int(utc.group(2)))))
        elif utc.group(1) == '-':
            cur_dt = dt.replace(tzinfo=timezone(timedelta(hours=int('-'+utc.group(2)))))
    ##用.astimezone()方法转换当前时区至UTC
    utc_dt = cur_dt.astimezone(timezone(timedelta(hours = 0)))
    return utc_dt.timestamp()##用.timestamp()方法转换UTC时间至timestamp


t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
print(t1)
t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
print(t2)


