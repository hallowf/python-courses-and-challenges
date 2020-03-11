from __future__ import print_function
try:
  input = raw_input
except NameError:
  pass

main_character = input("Name of the main character? ")
sidekick = input("Name of the sidekick? ")

print("%s went on an adventure with his trusty sidekick %s." % (main_character,sidekick))