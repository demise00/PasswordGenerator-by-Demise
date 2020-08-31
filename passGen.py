import random
import string

working = True
while working == True:
    lenght = int(input("How long do you want the password to be? [in numbers] "))
    wantNums = input("Do you want numbers in the password? [yes/no] ")
    wantUppers = input("Do you want uppercase letters? [yes/no] ")
    def passGen(lenght):
        password = ""
        upper_letters = string.ascii_uppercase
        lower_letters = string.ascii_lowercase
        letters = lower_letters + upper_letters
        numbers = "1234567890"
        all_chars = numbers + letters
        if wantNums.lower() == "yes" and wantUppers.lower() == "yes":
            password = password + random.choice(upper_letters)
            password = password + random.choice(numbers)
            for i in range(lenght-2):
                password = password + random.choice(all_chars) 
            print(password)

        elif wantNums.lower() == "no" and wantUppers.lower() == "yes":
            password = password + random.choice(upper_letters)
            for i in range(lenght-1):
                password = password + random.choice(all_chars)
            print(password)

        elif wantNums.lower() == "yes" and wantUppers.lower() == "no":
            password = password + random.choice(numbers)
            for i in range(lenght-1):
                password = password + random.choice(all_chars)
            print(password.lower())
        
        elif wantNums.lower() == "no" and wantUppers.lower() == "no":
            password = ""
            for i in range(lenght):
                password = password + random.choice(all_chars)
            print(password.lower())

        else:
            print("Invalid input, please enter yes or no! ")

    passGen(lenght)

    restart = input("Do you want another password? [yes/no] ")
    if restart.lower() == "yes":
        working = True
    else:
        print("Goodbye!")
        working = False
