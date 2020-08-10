import random
import string

while True:

    def ask_for_yes_no(question: str) -> bool:
        while True:
            answer = input(question + " [yes/no]: ").lower()
            if answer in ["yes", "no"]:
                break
            print("Please answer with yes or no!")

        return True if answer == "yes" else False

    def get_random_string(length: int,
                          include_num: bool=False,
                          include_uppercase: bool=False,
                          include_special_chars: bool=False) -> str:
        chars = string.ascii_lowercase
        if include_num:
            chars += string.digits
        if include_uppercase:
            chars += string.ascii_uppercase
        if include_special_chars:
            chars += string.punctuation

        return "".join(random.choices(chars, k=length))

    length = int(
        input("How long do you want the password to be? [in numbers]: "))

    include_num = ask_for_yes_no("Do you want numbers in the password?")

    include_uppercase = ask_for_yes_no("Do you want uppercase letters?")

    include_special_chars = ask_for_yes_no("Do you want special characters?")

    random_string = get_random_string(
        length=length,
        include_num=include_num,
        include_uppercase=include_uppercase,
        include_special_chars=include_special_chars)
    print(random_string)

    restart = ask_for_yes_no("Do you want another password?")
    if not restart:
        print("Goodbye!")
        break
