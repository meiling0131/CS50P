import random

def main():
    score = 0
    lev = get_level()
    for _ in range(10):
        x = generate_integer(lev)
        y = generate_integer(lev)
        for _ in range(3):
            try:
                result = int(input(f"{x} + {y} = "))
                if result == x + y:
                    score += 1
                    break
                else:
                    print("EEE")
            except ValueError:
                print("EEE")
        else:
            print(f"{x} + {y} = {x + y}")
    print("Score: ", score)

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 1 <= level <=3:
                return level
            else:
                raise ValueError
        except ValueError:
            pass

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    return random.randint(10 ** (level-1), 10 ** level - 1)

if __name__ == "__main__":
    main()