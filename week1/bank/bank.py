def bank(ans):
    ans = ans.strip().lower()
    if ans.startswith("hello") :
        return "$0"
    elif ans[0] == "h":
        return "$20"
    else:
        return "$100"

def main():
    print(bank(input("Greeting: ")))

if __name__ == "__main__":
    main()