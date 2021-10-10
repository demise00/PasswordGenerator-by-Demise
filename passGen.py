import random
import string

working = True
while working == True:

    lenght = int(input("[*] How long do you want the password to be? [in numbers] "))
    if lenght >= 8:
        def passGen(lenght):
            wantNums = input("[*] Do you want numbers in the password? [yes/no] ")
            wantUppers = input("[*] Do you want uppercase letters? [yes/no] ")
            if wantNums.lower() == "yes" and wantUppers.lower() == "yes":
                password = ""
                chars = string.ascii_letters + "1234567890"
                for i in range(lenght):
                    password = password + random.choice(chars)
                print(password)


            elif wantNums.lower() == "no" and wantUppers.lower() == "yes":
                password = ""
                chars = string.ascii_letters 
                for i in range(lenght):
                    password = password + random.choice(chars)
                print(password)

            elif wantNums.lower() == "yes" and wantUppers.lower() == "no":
                password = ""
                chars = string.ascii_letters + "1234567890"
                for i in range(lenght):
                    password = password + random.choice(chars)
                print(password.lower())
        
            elif wantNums.lower() == "no" and wantUppers.lower() == "no":
                password = ""
                chars = string.ascii_letters
                for i in range(lenght):
                    password = password + random.choice(chars)
                print(password.lower())

            else:
                print("Invalid input, please enter yes or no! ")
        passGen(lenght)
        restart = input("[?]Do you want another password? [yes/no] ")
        if restart == "yes":
            working = True
        else:
            print("Goodbye!")
            working = False
    else:
        print('[!] The password characters should be 8 or more.')
        again = input("[?] Do you want to try again? [yes/no] ")
        if again == "yes":
            working = True
        else:
            print("Goodbye!")
            working = False
