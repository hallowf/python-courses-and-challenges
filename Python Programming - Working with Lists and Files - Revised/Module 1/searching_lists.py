from __future__ import print_function

guests = ["Chris", "Susan", "Bill", "Satya", "Sonal"]

print(guests.index("Bill"))

for steps in range(len(guests)):
  print(guests[steps])

guests_updated = False
for guest in guests:
  print(guest)
  if guest == guests[-1] and not guests_updated:
    print("Last guest adding one more")
    guests.append("Somebody")
    guests_updated = True

print(guests)
