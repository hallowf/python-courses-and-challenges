from __future__ import print_function
try:
  input = raw_input
except NameError:
  pass

finished = False
guests = []

print("Please enter guests name (Type done when finished)")
while not finished:
  name = input(" ")
  if name.upper() != "DONE":
    guests.append(name.capitalize())
  else:
    finished = True

print("Guests are:")
for guest in guests:
  print(guest)