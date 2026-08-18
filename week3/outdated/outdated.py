def main():
    months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]
    while True:
        try:
            user_input = input("Date: ").strip()
            MM,DD,YYYY = user_input.split(' ')
            if MM not in months:
                continue
            MM = months.index(MM) + 1
            if DD[-1] == ",":
                DD = int(DD[:-1])
            else:
                continue
            if DD > 31:
                continue
            print(f"{YYYY}-{MM:02}-{DD:02}")
            break
        except ValueError:
            MM,DD,YYYY = user_input.split('/')
            if len(MM) > 2 or int(DD) > 31 or int(MM) > 12:
                continue
            print(f"{YYYY}-{int(MM):02}-{int(DD):02}")
            break


main()








