from __future__ import print_function
import sys
print('The capybara is the worlds largest rodent')
print("The capybara likes to live in groups")
print("The capybara can swim", file=sys.stdout)
print("It's a beautiful day in the neighborhood")
# Escaping characters
print('It\'s a beautiful day in the neighborhood')
print("Here's a url \\news")
# Multiple lines
print("It's a beautiful day")
print("In the neighborhood")
print("It's a beautiful day\nIn the neighborhood")
print('''It's a beautiful day
In the neighborhood''')
print("""It's a beautiful day
In the neighborhood""")
# Concatenation of strings
print("here is a string" + " here is more")
