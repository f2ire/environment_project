import calendar
import datetime

cal = calendar.Calendar()
for i in cal.itermonthdays4(2022, 4):
    if i[1] == datetime.date.today().month:
        print(i)
