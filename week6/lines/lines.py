import sys

def main():
    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].strip().endswith(".py"):
        sys.exit("Not a python file")
    try:
        with open(sys.argv[1]) as file:
            print(sum(1 for line in file if line.strip() and not line.lstrip().startswith("#")))
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()