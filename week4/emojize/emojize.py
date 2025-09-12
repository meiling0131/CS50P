from emoji import emojize

def main():
    emoji = input("Input: ")
    convert(emoji)

def convert(emoji):
    print("Output: ",emojize((emoji), language = "alias"))

if __name__ == "__main__":
    main()