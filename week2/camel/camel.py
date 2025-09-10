def main():
    snake_case = camelcase(input("camelCase: "))
    print(f"snake_case: {snake_case}")

def camelcase(s):
    result = ""
    for c in s.strip():
        if c.isupper():
            result += "_" + c.lower()
        else:
            result += c

    return result

if __name__ == "__main__":
    main()
