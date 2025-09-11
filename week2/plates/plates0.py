import re


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    pattern = re.compile(r'(?=.{2,6}$)[A-Za-z]{2}[A-Za-z]*(?:[1-9][0-9]*)?$')
    return bool(pattern.fullmatch(s))


if __name__ == "__main__":
    main()



