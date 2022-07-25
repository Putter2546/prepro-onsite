"""เบื่อแล้วขนมตู้ อยากเป็นชู้กับเธอ"""
def main():
    """print"""
    money = int(input())
    water = int(input())
    snack_count1 = int(input())
    snack_count2 = int(input())
    snack_count3 = int(input())
    cost = money - water
    snack_1 = cost % 3
    if snack_1 == 0:
        snack_num1 = 10 * snack_count1
    elif snack_1 == 1:
        snack_num1 = 15 * snack_count1
    elif snack_1 == 2:
        snack_num1 = 20 * snack_count1
    cost_2 = cost - snack_num1
    snack_2 = cost_2 % 3
    if snack_2 == 0:
        snack_num2 = 12 * snack_count2
    elif snack_2 == 1:
        snack_num2 = 15 * snack_count2
    elif snack_2 == 2:
        snack_num2 = 18 * snack_count2
    cost_3 = cost_2 - snack_num2
    snack_3 = cost_3 % 3
    if snack_3 == 0:
        snack_num3 = 5 * snack_count3
    elif snack_3 == 1:
        snack_num3 = 7 * snack_count3
    elif snack_3 == 2:
        snack_num3 = 9 * snack_count3
    cost_4 = cost_3 - snack_num3
    if cost_4 < 0:
        print("Now you have %d left." %money)
        print("You don't have enough money!")
    elif cost_4 >= 0:
        print("Now you have %d left." %cost_4)
        print("Here's your order!")
        print("Water: %d baht" %water)
        print("Snack number 1: %d baht" %snack_num1)
        print("Snack number 2: %d baht" %snack_num2)
        print("Snack number 3: %d baht" %snack_num3)
main()
