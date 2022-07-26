"""ตัวเลขที่มีอยู่"""

def main():
    """main Function"""
    tape = int(input())
    summa = 0
    if tape > 0:
        while True:
            length = input()
            if length == "No more!":
                break
            else:
                for i in range(1, tape):
                    if i == int(length):
                        summa += i
        if summa == 0:
            print("Not Found Number")
        else:
            print("Sum of Found Number = %d" %summa)
    else:
        print("No Tape Measure")
main()
