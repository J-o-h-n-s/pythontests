import string
import random
from os import system, name


letters = list(string.ascii_letters)
digits = list(string.digits)
special_characters = list("!@#$%^&*()£")
characters = list(string.ascii_letters + string.digits + '!@#$%^&*()£')

def clear():
    if name == 'nt':
        _ = system('CLS')

    else:
        _ = system('clear')

def generate_random_password():
    
    clear()

    length = int(input("Enter password length: "))
    amount = int(input('Enter amount of passwords: '))

    letters_count = int(input("Enter letter count: "))
    digits_count = int(input("Enter digits count: "))
    special_characters_count = int(input("Enter special characters count: "))

    character_count = letters_count + digits_count + special_characters_count

    if character_count > length -1:
        print("Characters total count is greater than desired password length")
        exit()

    clear()

    password = []
    print("Following passwords saved to Passwords.txt, please move the file before generating new passords, as a new generation will overwrite existing")
    print('\n')

    for pwd in range(amount):
        password = []
        for c in range(digits_count):
            password.append(random.choice(digits))

        for c in range(letters_count):
            password.append(random.choice(letters))

        for c in range(special_characters_count):
            password.append(random.choice(special_characters))

        if character_count < length:
            random.shuffle(characters)
            for c in range(length - character_count):
                password.append(random.choice(characters))

                random.shuffle(password)


            if str(password) < str(length):
                return()
            else:
                print("".join(password))


    with open("Passwords.txt", "w") as f:
        f.writelines(password)

generate_random_password()
