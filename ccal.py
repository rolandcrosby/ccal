import datetime
import calendar
import sys
import os

rows = int(os.popen('stty size', 'r').read().split()[0])
if rows == 0:
    rows = 25
today = datetime.date.today()
day = today - datetime.timedelta(today.isoweekday() % 7)
end = day + datetime.timedelta(7 * (rows - 1))
while day < end:
    sys.stdout.write('{:>3}'.format(day.day))
    if day.isoweekday() == 6:
        if day.day < 8:
            sys.stdout.write('  {0}'.format(calendar.month_name[day.month]))
        sys.stdout.write('\n')
    day += datetime.timedelta(1)
