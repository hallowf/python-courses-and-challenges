from __future__ import print_function, division
try:
  input = raw_input
except NameError:
  pass

import datetime

deadline = input("What is your project deadline? ")
deadline_date = datetime.datetime.strptime(deadline, "%d/%m/%Y").date()
current_date = datetime.date.today()
current_year = current_date.year


difference = deadline_date - current_date

days_remaining = difference.days
weeks_remaining = days_remaining / 7

week_s = "week" if weeks_remaining == 1  else "weeks"

print("Days remaining: %d %s, %s days" % (weeks_remaining,week_s,days_remaining))
