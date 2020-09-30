import random
import string

# creating some variables
working = True

# running while loop for asking to a user to run get your password again if you want
while working == True:

    # taking an input from user in a int type
    lenght = int(input("How long do you want the password to be? [in numbers] "))
    wantNums = input("Do you want numbers in the password? [yes/no] ")
    wantUppers = input("Do you want uppercase letters? [yes/no] ")


    
    def passGen(lenght):
        """Generating a Password"""
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

        

                
    # calling a function 
    passGen(lenght)
    
    # asking from user to that did he want to get a password again
    restart = input("Do you want another password? [yes/no] ")
    
    #checking that is user want a password again ot not
    if restart.lower() == "yes":
        working = True
    else:
        print("Goodbye!")
        working = False
