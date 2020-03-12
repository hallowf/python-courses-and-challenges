from __future__ import print_function
try:
  input = raw_input
except NameError:
  pass

print("I have %d cats" % 6)   # I have 6 cats
print("I have %3d cats" % 6)  # I have  6 cats
print("I have %03d cats" % 6) # I have 006 cats
print("I have %f cats" % 6)   # I have 6.000000 cats
print("I have %.2f cats" % 6) # I have 6.00 cats

print("I have {0:d} cats".format(6))   # I have 6 cats
print("I have {0:3d} cats".format(6))  # I have  6 cats
print("I have {0:03d} cats".format(6)) # I have 006 cats
print("I have {0:f} cats".format(6))   # I have 6.000000 cats
print("I have {0:.2f} cats".format(6)) # I have 6.00 cats
