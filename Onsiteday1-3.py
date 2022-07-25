"""Suvarnabhumi Airport"""
def main():
    """MAIN fUNCTION"""
    bangkok = input()
    destination = input()
    time = input()
    if destination == "To Sydney (SYD)":
        if time[6:8] == "PM":
            travel = time.replace("PM", "AM")
            print("BKK - SYD")
            print(travel)
        else:
            travel = time.replace("AM", "PM")
            print("BKK - SYD")
            print(travel)
    elif destination == "To Ho Chi Minh (SGN)":
        minute = int(time[3:5]) + 50
        minutes = minute % 60
        hours_min = minute // 60
        hours = int(time[0:2]) + 1 + hours_min
        print("BKK - SGN")
        print("%02d:%02d" %(hours, minutes))
main()
