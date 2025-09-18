import re
def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    if not re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", ip):
        return "False"

    for part in ip.split("."):
        if not part.isdigit():
            return "False"
        if int(part) != 0 and part.startswith("0"):
            return "False"
        if not 0 <= int(part) <= 255:
            return "False"
    return "True"

if __name__ == "__main__":
    main()