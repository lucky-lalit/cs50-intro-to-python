import sys


def main():
    if len(sys.argv) < 2:
        sys.exit('Too few command-line arguments')
    elif len(sys.argv) > 2:
        sys.exit('Too many command-line arguments')
    try:
        with open(sys.argv[1]) as f:
            if not sys.argv[1].endswith('.py'):
                sys.exit("Not a Python file")
            row = f.readlines()
            count = 0
            for line in row:
                line = line.strip()
                if not line.startswith('#') and line != "":
                    count = count + 1
    except FileNotFoundError:
        sys.exit("File does not exist")
    print(count)


main()
