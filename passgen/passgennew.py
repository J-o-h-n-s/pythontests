import string
import random

alphabets = list(string.ascii_letters)
digits = list(string.digits)
special_characters = list("!@#$%^&*()£")
characters = list(string.ascii_letters + string.digits + '!@#$%^&*()£')

def generate_random_password():
    length = int(input("Enter password length: "))
    amount = int(input('Enter amount of passwords: '))

    alphabets_count = int(input("Enter letter count: "))
    digits_count = int(input("Enter digits count: "))
    special_characters_count = int(input("Enter special characters count: "))

    character_count = alphabets_count + digits_count + special_characters_count

    if special_characters_count > length:
        print("Characters total count is greater than desired password length")
        return


    password = []

    for pwd in range(amount):
        password = []
        for c in range(digits_count):
            password.append(random.choice(digits))

        for c in range(alphabets_count):
            password.append(random.choice(alphabets))

        for c in range(special_characters_count):
            password.append(random.choice(special_characters))

        if character_count < length:
            random.shuffle(characters)
            for c in range(length - character_count):
                password.append(random.choice(characters))

                random.shuffle(password)



                print("".join(password))

                with open('Passowrds.txt', 'w') as file:
                    for line in password:
                        file.write(line)
                        file.write('\n')

generate_random_password()
