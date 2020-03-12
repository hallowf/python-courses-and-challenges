from __future__ import print_function

persons = [
           ["Doyle McCarty", 27],
           ["Jodi Mills", 25],
           ["Nicholas Rose", 32]
]

line_end = "\n"
with open("some_file.csv", "w") as fh:
  for info in persons:
    if info == persons[-1]:
      line_end = ""
    line = "%s, %d%s" % (info[0], info[1], line_end)
    fh.write(line)
