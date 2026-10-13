from datetime import date
import datetime
import inflect
import sys

p = inflect.engine()


def main():
    result = valid_date(input("Date of Birth: "))
    print(result)


def valid_date(ip):
    try:
        yy, mm, dd = ip.split('-')
        birth = date(int(yy), int(mm), int(dd))
        diff = date.today() - birth
        days_min = diff.days * 24 * 60
        words = p.number_to_words(days_min, andword="") + " minutes"
        return words.capitalize()

    except ValueError:
        sys.exit("Invalid date")


if __name__ == "__main__":
    main()
