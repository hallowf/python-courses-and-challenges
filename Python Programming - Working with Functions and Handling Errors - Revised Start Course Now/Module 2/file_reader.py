from __future__ import print_function
try:
  input = raw_input
except NameError:
  pass

file_name = input("Specify the file to open ")

try:
  with open(file_name, "r") as fh:
    print(fh.read())
except IOError:
  print("File not found: %s" % file_name)