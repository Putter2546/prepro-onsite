"""Atbash Cipher"""
def main():
    """main function"""
    text = input()
    for i in range(len(text)):
        ntext = ord(text[i])
        if 65 <= ntext <= 90:
            txt = 91 - ntext + 64
            txt = chr(txt)
            print(txt, end="")
        elif 97 <= ntext <= 122:
            txt = 123 - ntext + 96
            txt = chr(txt)
            print(txt, end="")
        else:
            print(text[i], end="")
            continue
main()
