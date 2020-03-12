from __future__ import print_function
try:
  input = raw_input
except NameError:
  pass

import datetime

birthday = input("What is your birthday? ")
print("Your birthday is %s" % birthday)
birthdate = datetime.datetime.strptime(birthday, "%d/%m/%Y").date()

print("Your birth month is %s" % birthdate.strftime("%B"))

current_date = datetime.date.today()
current_year = current_date.year

next_birthday = "%s/%s/%s" % (birthdate.day,birthdate.month,current_year)
print("Next birthday is %s" % next_birthday)
next_birthday  = datetime.datetime.strptime(next_birthday, "%d/%m/%Y").date()

difference = next_birthday - current_date

print("Days remaining: %s" % difference.days)
