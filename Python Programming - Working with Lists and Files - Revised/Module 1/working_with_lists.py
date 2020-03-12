from __future__ import print_function

guests = ["Chris", "Susan", "Bill", "Satya", "Sonal"]

guests.append("Colin")
guests.append("Sonal")

guests[3] = "Somebody"

guests.remove("Sonal")

del guests[0]

for guest in guests:
  print(guest)

guests.sort()

print(guests)

scores = [78,85,62,49,98]

print(scores[3])