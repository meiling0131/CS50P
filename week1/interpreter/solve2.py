def inter(exp):
    x, y, z =  exp.split()
    x, z = int(x), int(z)
    return eval(f"{x} {y} {z}")

def main():
    ans =inter(input("Expression: "))
    print(f"{ans:.1f}")

if __name__ == "__main__":
    main()