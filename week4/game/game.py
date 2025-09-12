from random import randint

def main():
    while True:
        try:
            level = int(input("Level: "))
            if level <= 0:
                raise ValueError
            break
        except ValueError:
            continue

    game(level)

def game(l):
    target = randint(1, l)
    while True:
        try:
            guess = int(input("Guess: "))
            if guess <= 0:
                raise ValueError
            if guess < target:
                print("Too small!")
            elif guess > target:
                print("Too Large!")
            else:
                print("Just right!")
                break
        except ValueError:
            continue

if __name__ == "__main__":
    main()