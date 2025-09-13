def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if not 2 <= len(s) <= 6:
        return False
    elif not s.isalnum():
        return False
    elif not s[0].isalpha() or not s[1].isalpha():
        return False

    is_digit = False
    for ch in s:
        if ch.isdigit():
            if ch == "0" and not is_digit:
                return False
            else:
                is_digit = True
        else:
            if ch.isalpha() and is_digit:
                return False
    return True

if __name__ == "__main__":
    main()