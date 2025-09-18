import re

def main():
    print(parse(input("HTML: ")))

def parse(s):
    pattern = r'<iframe.*?src="(https?:\/\/(?:www\.)?youtube\.com(?:\/embed)?\/[a-zA-z0-9_-]+)".*?'
    if match := re.match(pattern, s):
        url = match.group(1).split("/")[-1]
        return f"https://www.youtu.be/{url}"
    return None

if __name__ == "__main__":
    main()