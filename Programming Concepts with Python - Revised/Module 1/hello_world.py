#Retain backwards compatibility with python 2
from __future__ import print_function
print("Hello World!")

# Write to system standard output
import sys
print("Hello World!\n", file=sys.stdout)
