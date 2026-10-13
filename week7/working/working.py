import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    match = re.search(
        r"^([1-9]|1[0-2])(:[0-5][0-9])? (AM|PM) to ([1-9]|1[0-2])(:[0-5][0-9])? (PM|AM)$", s)
    if match:
        if match.group(3) == 'AM':
            hr_am = int(match.group(1))
            if hr_am == 12:
                hr_am = 0
            if not match.group(2):
                min_am = 0
            else:
                min_am = int(match.group(2)[1:])
            if int(match.group(4)) == 12:
                hr_pm = 12
            else:
                hr_pm = int(match.group(4)) + 12
            if not match.group(5):
                min_pm = 0
            else:
                min_pm = int(match.group(5)[1:])
            return f"{hr_am:02}:{min_am:02} to {hr_pm:02}:{min_pm:02}"
        else:
            if int(match.group(1)) == 12:
                hr_pm = 12
            else:
                hr_pm = int(match.group(1)) + 12
            if not match.group(2):
                min_pm = 0
            else:
                min_pm = int(match.group(2)[1:])
            hr_am = int(match.group(4))
            if hr_am == 12:
                hr_am = 0
            if not match.group(5):
                min_am = 0
            else:
                min_am = int(match.group(5)[1:])
            return f"{hr_pm:02}:{min_pm:02} to {hr_am:02}:{min_am:02}"
    raise ValueError


if __name__ == "__main__":
    main()
