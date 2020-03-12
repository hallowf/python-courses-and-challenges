from __future__ import print_function

def main():
  names = get_names()
  print_names(names)

def get_names():
  names =  ["Chris", "Susan", "Danny"]
  last_name = "Waldo"
  names.append(last_name)
  return names

def print_names(names):
  for name in names:
    print(name)

if __name__ == "__main__":
  main()