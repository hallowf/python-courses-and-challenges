from __future__ import print_function
try:
  input = raw_input
except NameError:
  pass

salary = input("Please enter your salary ")
bonus = input("Please enter your bonus ")

paycheck_amount = float(salary) + float(bonus)

print(paycheck_amount)