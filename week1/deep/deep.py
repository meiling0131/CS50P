def answer(ans):
    return "Yes" if ans.strip().lower() in {"forty-two", "forty two", "42"} else "NO"

def main():
    print(answer(input("What is the answer to the Great Question of Life, the Universe and Everything? ")))

if __name__ == "__main__":
    main()