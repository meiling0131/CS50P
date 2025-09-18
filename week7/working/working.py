import re

def main():
    print(convert(input("Hours: ")))


def convert(s):
    # Regex pattern to match the required formats
    pattern = r"^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$"

    match = re.match(pattern, s)
    if not match:
        raise ValueError("Invalid format")

    # Extract matched groups
    start_hour, start_min, start_period, end_hour, end_min, end_period = match.groups()

    # Convert to integers
    start_hour = int(start_hour)
    end_hour = int(end_hour)
    start_min = int(start_min) if start_min else 0
    end_min = int(end_min) if end_min else 0

    # Validate hours and minutes
    if not (1 <= start_hour <= 12) or not (1 <= end_hour <= 12):
        raise ValueError("Invalid hour")
    if not (0 <= start_min <= 59) or not (0 <= end_min <= 59):
        raise ValueError("Invalid minute")

    def to_24_hour(hour, period):
        if period == "AM":
            if hour == 12:
                return 0
            else:
                return hour
        else:  # PM
            if hour == 12:
                return 12
            else:
                return hour + 12

    start_24 = to_24_hour(start_hour, start_period)
    end_24 = to_24_hour(end_hour, end_period)

    start_formatted = f"{start_24:02d}:{start_min:02d}"
    end_formatted = f"{end_24:02d}:{end_min:02d}"

    return f"{start_formatted} to {end_formatted}"


if __name__ == "__main__":
    main()