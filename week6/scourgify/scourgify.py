import sys
import csv

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if not sys.argv[1].strip().endswith(".csv"):
        sys.exit("Not a CSV file")
    try:
        with open(sys.argv[1]) as input, open(sys.argv[2]) as output:
            reader = csv.DictReader(input)
            fieldnames = ["first", "last", "house"]
            writer = csv.DictWriter(output, fieldnames=fieldnames)
            writer.writeheader()

            for row in reader:
                last_name, first_name = [s.strip() for s in row["name"].strip().split(",")]
                writer.writerow({
                    "first": first_name,
                    "last": last_name,
                    "house": row["house"]
                })

    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()