"""Usage:
    ccal
    ccal <year>
    ccal <month> <year>"""

import datetime
import calendar
import sys
import os
from docopt import docopt

def write_cal(start, end, dest=sys.stdout):
    day = start - datetime.timedelta(start.isoweekday() % 7)
    end = end + datetime.timedelta(7 - end.isoweekday())
    while day < end:
        dest.write('{:>3}'.format(day.day))
        if day.isoweekday() == 6:
            if day.day < 8:
                dest.write('  {0}'.format(calendar.month_name[day.month]))
            dest.write('\n')
        day += datetime.timedelta(1)

if __name__ == "__main__":
    args = docopt(__doc__)
    print args
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
        rows = int(os.popen('stty size', 'r').read().split()[0])
        if rows == 0:
            rows = 25
        today = datetime.date.today()
        start = today - datetime.timedelta(today.isoweekday() % 7)
        end = start + datetime.timedelta(7 * (rows - 1))
    write_cal(start, end)

