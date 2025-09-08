import re

while True:
    email = input("What's your email? ").strip()

    if re.search(r"^(\w.)+@(\w+\.)?\w+\.(com|edu|gov|org)$", email, re.IGNORECASE):
        print("Valid")
        break
    else:
        print("Invalid email. Please try again.")
