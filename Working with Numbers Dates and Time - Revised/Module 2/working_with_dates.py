from __future__ import print_function
try:
  input = raw_input
except NameError:
  pass

import datetime

current_date = datetime.date.today()

print(current_date)

current_year = current_date.year
current_month = current_date.month
current_day = current_date.day

print(current_year)
print(current_month)
print(current_day)

# changing date format
print(current_date.strftime("%d %b,%Y"))

# Sentence with date
print(current_date.strftime("Please attend our event %A, %B %d  in the year %Y"))
