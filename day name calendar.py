import calendar
mo, da, ye = map(int, input().split())
weekday = calendar.day_name[calendar.weekday(ye, mo, da)].upper()
print(calendar.month(ye, mo, w=1, l=1))
print(weekday)
