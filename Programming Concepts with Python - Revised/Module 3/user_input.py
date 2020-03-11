from __future__ import print_function
try:
  input = raw_input
except NameError:
  pass

name = input("What is your name? ")

print("Hello %s" % name)

name = "something else"

print("Hello %s" % name)