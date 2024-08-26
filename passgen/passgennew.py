import string
import random
from os import system, name


letters = string.ascii_letters
digits = string.digits
special_characters = "!@#$%^&*()£"
characters = string.ascii_letters + string.digits + "!@#$%^&*()£"


def clear():
    if name == "nt":
        _ = system("CLS")

    else:
        _ = system("clear")


def generate_random_password():

    clear()

    length = int(input("Enter password length: "))
    amount = int(input("Enter amount of passwords: "))

    letters_count = int(input("Enter letter count: "))
    digits_count = int(input("Enter digits count: "))
    special_characters_count = int(input("Enter special characters count: "))

    character_count = letters_count + digits_count + special_characters_count

    if character_count > length - 1:
        print("Characters total count is greater than desired password length")
        exit()

    clear()

    print(
        "Following passwords saved to Passwords.txt, please move the file before generating new passords, as a new generation will overwrite existing"
    )
    print("\n")

    extra_characters_count = length - character_count
    passwords = []
    for _ in range(amount):
        chosen_digits = random.choices(digits, k=digits_count)
        chosen_letters = random.choices(letters, k=letters_count)
        chosen_special_characters = random.choices(
            special_characters, k=special_characters_count
        )

        extra_characters = random.choices(characters, k=extra_characters_count)

        password = (
            chosen_digits
            + chosen_letters
            + chosen_special_characters
            + extra_characters
        )
        random.shuffle(password)
        password.append("\n")
        passwords.append("".join(password))

        if str(password) < str(length):
            return ()
        else:
            print("".join(password))

    with open("Passwords.txt", "w") as f:
        f.writelines(passwords)


generate_random_password()
