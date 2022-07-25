"""Drop Drop"""
def main():
    """print"""
    grade = float(input())
    if grade < 1.00:
        print("I'm so sad.")
    elif 1.00 <= grade < 2.00:
        gradetwo = 4.00 - grade
        print("%.2f" %gradetwo)
    elif 4.00 >= grade >= 2.00:
        print("I'm so happy.")
main()
