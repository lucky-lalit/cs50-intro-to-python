from tabulate import tabulate
import sys
import csv
menu = []


def main():
    if len(sys.argv) < 2:
        sys.exit('Too few command-line arguments')
    elif len(sys.argv) > 2:
        sys.exit('Too many command-line arguments')
    try:
        with open(sys.argv[1]) as f:
            if not sys.argv[1].endswith('.csv'):
                sys.exit("Not a CSV file")
            reader = csv.reader(f)
            for row in reader:
                menu.append(row)
            header = menu[0]
            table = menu[1:]
    except FileNotFoundError:
        sys.exit("File does not exist")
    print(tabulate(table, header, tablefmt="grid"))


main()
