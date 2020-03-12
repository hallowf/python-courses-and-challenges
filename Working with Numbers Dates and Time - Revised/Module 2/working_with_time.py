from __future__ import print_function
try:
  input = raw_input
except NameError:
  pass

import datetime

current_date = datetime.datetime.now()
print(current_date.minute)