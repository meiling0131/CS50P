def main():
    input_word = input("Input: ").strip()
    output_word = shorten(input_word)
    print("Output: ", output_word)

def shorten(word):
    for ch in word:
        if ch in "aeiouAEIOU":
            word = word.replace(ch, "")
    return word

if __name__ == "__main__":
    main()