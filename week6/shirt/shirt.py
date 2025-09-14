import sys
from PIL import Image, ImageOps

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) < 3:
    sys.exit("Too many command-line arguments")
elif not sys.argv[2].endswith((".jpg", ".jpeg", ".png")):
    sys.exit("Invalid output")
elif  not sys.argv[1].split(".")[1] == sys.argv[2].split(".")[1]:
    sys.exit("Input and output have different extensions")


try:
    with Image.open("shirt.png") as shirt, Image.open(sys.argv[1]) as img:
        img = ImageOps.fit(img, shirt.size)
        img.paste(shirt, shirt)
        img.save(sys.argv[2])
except FileNotFoundError:
    sys.exit("Input does not exist")

