"""Usage:
    ccal
    ccal <year>
    ccal <month> <year>"""

import datetime
import calendar
import sys
import os
from docopt import docopt
import colors   # https://pypi.python.org/pypi/ansicolors/

def write_cal(start, end, dest=sys.stdout):
    day = start - datetime.timedelta(start.isoweekday() % 7)
    end = end + datetime.timedelta(7 - end.isoweekday())
    today = datetime.date.today()
    while day < end:
        day_string = '{:>3}'.format(day.day)
        if day == today:
            day_string = colors.red(day_string)
        dest.write(day_string)
        if day.isoweekday() == 6:
            if day.day < 8:
                out = '  {0}'.format(calendar.month_name[day.month])
                if day.month == 1:
                    out = out + ' {0}'.format(day.year)
                dest.write(out)
            dest.write('\n')
        day += datetime.timedelta(1)

def main():
    args = docopt(__doc__)
    if args['<year>'] is not None:
        year = int(args['<year>'])
        if args['<month>'] is not None:
            month = int(args['<month>'])
            start = datetime.date(year, month, 1)
            end = datetime.date(year, month, calendar.monthrange(year, month)[1])
        else:
            start = datetime.date(year, 1, 1)
            end = datetime.date(year, 12, 31)
    else:
        rows = int(os.popen('stty size', 'r').read().split()[0]) - 2
        if rows == 0:
            rows = 52
        today = datetime.date.today()
        start = datetime.date(today.year, today.month, 1)
        start = start - datetime.timedelta(start.isoweekday() % 7)
        end = start + datetime.timedelta(7 * rows)
    write_cal(start, end)
