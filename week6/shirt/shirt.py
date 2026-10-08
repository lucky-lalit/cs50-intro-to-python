import sys
import os
from PIL import Image, ImageOps

extension = ['.jpg', '.jpeg', '.png']


def main():
    if len(sys.argv) < 3:
        sys.exit('Too few command-line arguments')
    elif len(sys.argv) > 3:
        sys.exit('Too many command-line arguments')
    try:
        f1_name, f1_exten = os.path.splitext(sys.argv[1])
        f2_name, f2_exten = os.path.splitext(sys.argv[2])
        if f1_exten not in extension or f2_exten not in extension:
            sys.exit("Invalid output")
        if f1_exten != f2_exten:
            sys.exit("Input and output have different extensions")
        with Image.open(sys.argv[1]) as img, Image.open("shirt.png") as img2:
            img = ImageOps.fit(img, size=(600, 600))
            img.paste(img2, mask=img2)
            img.save(sys.argv[2])
    except FileNotFoundError:
        sys.exit("Input does not exist")


main()
