dates = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}
def main():
    while True:
        try:
            date = input("Date: ").strip()
            if "/" in date:
                date = date.strip().split("/")
                if int(date[0]) > 12 or int(date[1]) > 31:
                    continue
                digit(date)
                break
            elif "," in date:
                date = date.strip().replace(",","").split()
                if date[0] in dates and int(date[1]) < 32:
                    alpha(date)
                    break
                else:
                    continue
        except ValueError:
            continue


def digit(d):
    print(f"{int(d[2])}-{int(d[0]):02d}-{int(d[1]):02d}")
        
def alpha(a):
    print(f"{int(a[2])}-{int(dates[a[0]]):02d}-{int(a[1]):02d}")
    
if __name__ == "__main__":
    main()