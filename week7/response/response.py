import validators

if validators.email(input("What's your email?")):
    print("Valid")
else:
    print("Invalid")