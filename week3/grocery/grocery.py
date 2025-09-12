groceries = {}

while True:
    try:
        item = input().upper().strip()
        groceries[item] =groceries.get(item, 0) + 1
    except EOFError:
        break

for item in sorted(groceries):
    print(f"{groceries[item]} {item}")
