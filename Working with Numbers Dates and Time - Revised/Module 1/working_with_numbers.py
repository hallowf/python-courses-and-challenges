from __future__ import print_function
try:
  input = raw_input
except NameError:
  pass

area = 0
height = 10
width = 20

# calculate area of triangle
area = width * height / 2

# print float with 2 decimals
print("The area of the triangle would be %.2f" % area)

print("Favorite number is %d" % 42)

print("the area of the triangle would be {0:f}".format(area))

print("Favorite number is {0:d}".format(42))

# print multiple numbers
print("Here are two numbers! " + \
  "The first is {0:d}, The second is {1:3d}".format(1,2))