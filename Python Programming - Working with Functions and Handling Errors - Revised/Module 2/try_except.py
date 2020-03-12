from __future__ import print_function
import sys

try:
  input = raw_input
except NameError:
  pass

def get_number(number_pos):
  float_number = input("Enter the %s number " % number_pos)
  try:
    float_number = float(float_number)
    return float_number
  except ValueError:
    get_number(number_pos)
  except:
    error = sys.exc_info()[0]
    print("Something went wrong")
    print(error)
    raise

first_number = get_number("first")
second_number = get_number("second")

try:
  result = first_number / second_number
  print(str(first_number) + " / " + str(second_number) + " = " + str(result))
except ZeroDivisionError:
  print("You can't divide by zero")
  sys.exit()
except Exception as e:
  error = sys.exc_info()[0]
  print("Something went wrong")
  print(error)
  raise e
finally:
  print("This always runs")
print("This message only appears when no exceptions are raised")
