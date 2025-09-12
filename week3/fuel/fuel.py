while True:
    try:
        fuel = input("Fraction: ").strip().split("/")
        fuel[0] = int(fuel[0])
        fuel[1] = int(fuel[1])
        result = fuel[0] / fuel[1]
        if  result < 0 or result > 1:
            continue
        print(result)
        break
    except ValueError:
        continue
    except ZeroDivisionError:
        continue




