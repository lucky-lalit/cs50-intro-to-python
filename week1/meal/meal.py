def main():
    user_input = input("What time is it? ").strip()
    result = convert(user_input)
    if  7 <= result <= 8:
        print('breakfast time')
    elif 12 <= result <= 13:
        print('lunch time')
    elif 18 <= result <= 19:
        print('dinner time')
    # return float(user_input.replace(':','.'))



def convert(time):
    hour,minutes = time.split(":")
    # print(hour,minutes)
    original_hr = (int(hour) * 60 ) + int(minutes)
    # print('debug',original_hr)
    # hour = int(hour) % 12
    # minutes = int(minutes)
    # total_time = (hour * 60) + minutes
    return round(original_hr / 60,2)
    # if 1080 <= original_hr <= 1140:
    #     print('lunch time')
    #     # print(f"{total_time / 60 :.1f}")
    #     # return float(time.replace(':','.'))
    #     return round(original_hr / 60,2)
    #     return total_time
    #     return round(total_time / 60,1)
    # # return round(original_hr / 60,2)
    # elif 420 <= total_time <= 480:
    #     print('breakfast time')
    #     return round(original_hr / 60,2)
    #     return float(time.replace(':','.'))
    # elif 360 <= total_time <= 420:
    #     print('dinner time')
    #     # return total_time
    #     return round(original_hr / 60,2)
    #     return float(time.replace(':','.'))

if __name__ == "__main__":
    main()
