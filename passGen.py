import random
import string

working = True
while working == True:


    lenght = int(input("How long do you want the password to be? [in numbers] "))
    wantNums = input("Do you want numbers in the password? [yes/no] ")
    wantUppers = input("Do you want uppercase letters? [yes/no] ")


    def passGen(lenght):
        if length < 8:
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
         else:
            print("The length of password should be highter then 8 characters")

                

    passGen(lenght)

    restart = input("Do you want another password? [yes/no] ")
    if restart.lower() == "yes":
        working = True
    else:
        print("Goodbye!")
        working = False
