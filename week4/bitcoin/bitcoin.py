import requests
import sys

try:
    r = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=21179f6b3f881a561587761576b9c4c9e975ef21ce670855bcb2a0eeb922ea66")
    r.raise_for_status()
    data = r.json()
except requests.RequestException:
    sys.exit("Request Exception")

if len(sys.argv) < 2:
    sys.exit("Missing command-line argument")

try:
    amount = float(sys.argv[1])
except ValueError:
        sys.exit("Command-line argument is not a number ")

price = float(data["data"]["priceUsd"]) * float(sys.argv[1])
print(f"${price:,.4f}")
