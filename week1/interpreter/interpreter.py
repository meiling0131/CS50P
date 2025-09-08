def interpret(s):
    s = s.strip().lower()
    if "+" in s:
        parts = s.split("+")
        return float(parts[0]) + float(parts[1])
    if "-" in s:
        parts = s.split("-")
        return float(parts[0]) - float(parts[1])
    if "*" in s:
        parts = s.split("*")
        return float(parts[0]) * float(parts[1])
    if "/" in s:
        parts = s.split("/")
        return float(parts[0]) / float(parts[1])

def main():
    print(interpret(input("Expression: ")))

if __name__ == "__main__":
    main()