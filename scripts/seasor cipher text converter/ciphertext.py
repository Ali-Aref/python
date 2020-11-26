# by Ali Aref Mohammadi


# encrypt
def cipherEncrypt(plainText, shift):
    cipher = ''
    for char in plainText:
        if char == ' ':
            cipher = cipher + char
        elif char.isupper():
            # 65 is the 'A' unicode you check it by ord('A')
            cipher = cipher + chr((ord(char) + shift - 65) % 26 + 65)
        else:
            # 97 is the 'a' unicode you check it by ord('a')
            cipher = cipher + chr((ord(char) + shift - 97) % 26 + 97)

    return cipher


# decrypt
def cipherDecrypt(decryptedText, shift):
    plainText = ''
    for char in decryptedText:
        if char == ' ':
            plainText = plainText + char
        elif char.isupper():
            # 65 is the 'A' unicode you check it by ord('A')
            plainText = plainText + chr((ord(char) - shift - 65) % 26 + 65)
        else:
            # 97 is the 'a' unicode you check it by ord('a')
            plainText = plainText + chr((ord(char) - shift - 97) % 26 + 97)

    return plainText


def run():
    welcomeMessage = """
_________________________________________________________________________________________
|                                                                                       |
|    ************    *****   ***************     ************    ***************        |
|    ************    *****   ***************     ************    ***************        |
|    ***             *****   ****        ***     ***             ****        ***        |
|    ***             *****   ****        ***     ***             ****        ***        |
|    ***             *****   ***************     ************    ***************        |
|    ***             *****   ***************     ************    ***************        |
|    ***             *****   ****                ***             **** ***               |
|    ***             *****   ****                ***             ****   ***             |
|    ************    *****   ****                ************    ****      ***          |
|    ************    *****   ****                ************    ****        *** TEXT   |
|    (Written by Ali Aref Mohammadi Powered by PYTHON3.8)                               |
|_______________________________________________________________________________________|

    Welcome to Cipher Text encryption and decryption with python..
    Please choose from the following options:
    [1] Encrypt
    [2] Decrypt
    [3] Test
    [4] Exit
    """
    print(welcomeMessage[:welcomeMessage.index("Please")])
    exit = False
    while not exit:
        print("\n" + welcomeMessage[welcomeMessage.index("Please"):])
        try:
            mod = int(input())
            if mod == 1:
                text = input("Enter your text : ")
                shift = int(input("Enter Shift Number : "))
                print(f'The Encrypted Text is : {cipherEncrypt(text, shift)}')
            elif mod == 2:
                text = input("Enter your Cipher Encrypted text : ")
                shift = int(input("Enter Shift Number : "))
                print(f'The Decrypted Text is : {cipherDecrypt(text, shift)}')
            elif mod == 3:
                text = input("Enter your text : ")
                shift = int(input("Enter Shift Number : "))
                print(f'The Encrypted Text is : {cipherEncrypt(text, shift)}')
                print(f'The Decrypted Text is : {cipherDecrypt(cipherEncrypt(text, shift), shift)}')
            elif mod == 4:
                exit = True
                print("Thanks for using this script.. :)")
        except ValueError as e:
            print(e)


run()
