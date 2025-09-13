def main():
    while True:
        try:
            percentage = convert(input("Input: "))
            break
        except (ValueError, ZeroDivisionError):
            pass
    print(gauge(percentage))



def convert(fraction: str) -> int:
    x, y = map(int, fraction.split("/"))
    if y == 0:
        raise ZeroDivisionError
    percent = round(x / y * 100)
    if percent < 0 or percent > 100:
        raise ValueError
    return int(percent)

def gauge(percentage: int) -> str:
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()