def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    #here can only use if not, otherwise it can't return correctly
    if not 2 <= len(s) <= 6 :
        return False
    if not (s[0].isalpha() and s[1].isalpha()):
        return False
    if not s.isalnum():
        return False

    #if we see digit and then see another ch, return false
    seen_digit = False
    i = 0
    for ch in s:
        i += 1
        if ch.isdigit():
            if int(ch) == 0 and s[0:i-1].isalpha():
                return False
            seen_digit = True
        else:
            if seen_digit:
                return False
    return True

if __name__ =="__main__":
    main()