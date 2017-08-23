from enum import Enum, unique
#Enum类：枚举类
@unique
class Weekdays(Enum):
    Sun=0
    Mon=1
    Tue=2
    Wed=3
    Thu=4
    Fri=5
    Sat=6

print(Weekdays.Fri)
print(Weekdays(1))