import random
import os;
import pyperclip as pc;
import tkinter as tk;

#Tkinter configs
window = tk.Tk()

passWordLabel = tk.Label(window, text="Service password is for?")
passWordLabel.pack()

password_var = tk.StringVar()
passwordService = tk.Entry(window, textvariable=password_var, font=('calibre', 10, 'normal'))
passwordService.pack()


lengthLabel = tk.Label(window, text="Password length?")
lengthLabel.pack()
length_var = tk.IntVar()
lengthPw = tk.Entry(window, textvariable=length_var)
lengthPw.pack()


specCharacterLabel = tk.Label(window, text="Special characters?")
specCharacterLabel.pack()
spceChar_var = tk.BooleanVar()
specCharLabel = tk.Entry(window, textvariable=spceChar_var, text="t/f")
specCharLabel.pack()

window.mainloop()   



#user input areas
#passwordService = input("What service is this password for? ")
#lengthPw = int(input("Enter a password length between 1-64:"))
specCharacter = input("Special characters (True/False):") 


#function definitions
def generatePassword(length, specChar):
    randomPassword = []
    passLength = 0

    if "t" in specChar.lower():
        while length > passLength:
            charType = random.randrange(0,4)
            if charType == 0:
                newChar = str(generateNumber())
                passLength += 1
                randomPassword.append(newChar)
            if charType == 1:
                newChar = generateLowercase()
                randomPassword.append(newChar)
                passLength += 1
            if charType == 2:
                newChar = generateCapital()
                randomPassword.append(newChar)
                passLength += 1
            if charType == 3:
                newChar = str(generateSymbol())
                randomPassword.append(newChar)
                passLength += 1
    if specCharacter == "false" or specCharacter == "f" or specCharacter == "no":
        while length > passLength:
            charType = random.randrange(0,3)
            if charType == 0:
                newChar = str(generateNumber())
                passLength += 1
                randomPassword.append(newChar)
            if charType == 1:
                newChar = generateLowercase()
                randomPassword.append(newChar)
                passLength += 1
            if charType == 2:
                newChar = generateCapital()
                randomPassword.append(newChar)
                passLength += 1
    passAsString = ''.join(randomPassword)
    return passAsString


def generateNumber():
    num = random.randrange(1,10)
    return num

def generateLowercase():
    num = random.randrange(97,123)
    num = chr(num)
    return num

def generateCapital():
    num = random.randrange(65,91)
    num = chr(num)
    return num

#Rework this function, most websites don't allow excape keys in passwords. 
def generateSymbol():
    num = random.randrange(33,48)
    num = chr(num)
    return num

newPass = generatePassword(lengthPw, specCharacter)
print(f'{passwordService}: {newPass}')

clipboard = input('Copy to clipboard? (Y/N): ')

if clipboard.lower() in ["y", "yes"]:
    pc.copy(f'{passwordService}: {newPass}')
elif clipboard.lower() in ["n", "no"]:
    pass 
else:
    print("Invalid input. Please enter Y, N, Yes, or No.")

input('Press ENTER to continue')