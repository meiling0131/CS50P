def main():
    time = convert(input("What time is it? "))
    if (7.0 <= time <= 8.0):
        print("breakfast time")
    if (12.0 <= time <= 13.0):
        print("lunch time")
    if (18.0 <= time <= 19.0):
        print("dinner time")

def convert(time):
    time = time.strip().split(":")
    deci = float(time[1]) / 60
    return float(time[0]) + deci

if __name__ == "__main__":
    main()

