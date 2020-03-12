
def main():
  write_to_file("some text","some_file.txt")

def write_to_file(text,name_of_file):
  with open(name_of_file, "w") as fh:
    fh.write(text)

if __name__ == "__main__":
  main()