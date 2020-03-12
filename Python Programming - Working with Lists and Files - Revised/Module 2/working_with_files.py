from __future__ import print_function

file_name = "some_file.txt"

with open(file_name, "w") as fh:
  fh.write("some text")

with open(file_name, "r") as fh:
  print(fh.read())