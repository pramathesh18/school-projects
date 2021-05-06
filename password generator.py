import random

# This is created by Agneeva Guha
# This is my first time trying this type of program

border = "---------------*---------------"
print("Welcome to Password Generator : ")
print(border)

Password = ""
alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
         "w", "x", "y", "z"]
num = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
sym = ["@", "#", "%", "&", "*", "_", "-", "$", "!"]
CombinedList = [alpha, num, sym]
print("What kind of password do you want?\n"
      "Press 1 for Completely Random Password\n"
      "Press 2 for Partially Random Password")
passRandomComplete = int(input("Enter your choice (Any other choice will be treated as partially random) - ")) == 1
if passRandomComplete:
    print("-----------------------------------------")
    print("Choice taken - Completely Random Password")
    print("-----------------------------------------")
    nNum = 0
    nSym = 0
    nPassNum = 0
    nPassSym = 0
    if input("Do you want numbers in your password (Y or N) - ") == "Y":
        nNum = int(input("How many numbers do you want - "))
    if input("Do you want symbols in your password (Y or N) - ") == "Y":
        nSym = int(input("How many symbols do you want - "))
    PassLength = int(input("How long do you want the password to be (10 recommended) - "))
    while True:
        randlist = random.randint(0, len(CombinedList) - 1)
        randalpha = random.randint(0, len(alpha) - 1)
        randnum = random.randint(0, len(num) - 1)
        randsym = random.randint(0, len(sym) - 1)
        isUpperCase = random.randint(0, 1)
        if randlist == 0:
            if isUpperCase == 1:
                Password += CombinedList[randlist][randalpha].upper()
            else:
                Password += CombinedList[randlist][randalpha]
        elif randlist == 1 and nNum != 0:
            if nPassNum == nNum or len(Password) == 0:
                continue
            Password += CombinedList[randlist][randnum]
            nPassNum += 1
        elif randlist == 2 and nSym != 0:
            if nPassSym == nSym or len(Password) == 0:
                continue
            Password += CombinedList[randlist][randsym]
            nPassSym += 1
        PassOkay = False
        if len(Password) == PassLength:
            if nSym == nPassSym and nNum == nPassNum:
                print(border)
                print("Generated Password -", Password)
                if input("Is the password okay? (Y or N) - ").upper() == "Y":
                    PassOkay = True
                else:
                    Password = ""
                    nPassNum = 0
                    nPassSym = 0
            else:
                Password = ""
                nPassNum = 0
                nPassSym = 0
        if PassOkay:
            print(border)
            break
else:
    print("----------------------------------------")
    print("Choice taken - Partially Random Password")
    print("----------------------------------------")
    defpart = input("Enter the static part of your password - ")
    print("How would you want the random part in the Password?\n"
          "Press 1 for left indent (random_part-[defined_part])\n"
          "Press 2 for right indent ([defined_part]-random_part)\n"
          "{Right indent is recommended} - ", end="")
    randomindent = int(input())
    PassLength = int(input("How long do you want the whole password to be (15 recommended) - "))
    def_less_than_pass_length = True
    if PassLength <= len(defpart):
        print("The static part is longer than or equal to the total password length")
        def_less_than_pass_length = False
    randlength = PassLength - len(defpart) - 1
    Password = defpart
    while True:
        if not def_less_than_pass_length:
            break
        if randomindent == 1:
            randnum = random.randint(0, len(num) - 1)
            Password = num[randnum] + Password
        elif randomindent == 2:
            randnum = random.randint(0, len(num) - 1)
            Password += num[randnum]
        PassOkay = False
        if len(Password) == PassLength:
            print("Generated Password -", Password)
            if input("Is the password okay? (Y or N) - ") == "Y":
                PassOkay = True
            else:
                Password = defpart
        if PassOkay:
            break
