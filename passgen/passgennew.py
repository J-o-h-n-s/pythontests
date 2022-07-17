import string
import random
from os import system, name


alphabets = list(string.ascii_letters)
digits = list(string.digits)
special_characters = list("!@#$%^&*()£")
characters = list(string.ascii_letters + string.digits + '!@#$%^&*()£')

def clear():
    if name == 'nt':
        _ = system('CLS')

    else:
        _ = system('clear')

def generate_random_password():
    length = int(input("Enter password length: "))
    amount = int(input('Enter amount of passwords: '))

    alphabets_count = int(input("Enter letter count: "))
    digits_count = int(input("Enter digits count: "))
    special_characters_count = int(input("Enter special characters count: "))

#    if alphabets_count != int:
#        print('Number of letters is not a number')
#        exit()
#    if digits_count != int:
#        print('Number of digits is not a number')
#        exit()
#    if special_characters_count != int:
#        print('Number of special characters is not a number')
#        exit()

    character_count = alphabets_count + digits_count + special_characters_count

    if character_count > length:
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

        for c in range(alphabets_count):
            password.append(random.choice(alphabets))

        for c in range(special_characters_count):
            password.append(random.choice(special_characters))

        if character_count < length:
            random.shuffle(characters)
            for e in range(length - character_count):
                password.append(random.choice(characters))

                random.shuffle(password)


            if str(password) < str(length):
                print('Error')
            else:
                print("".join(password))


#            with open('Passowrds.txt', 'w') as file:
#                for line in str(password):
#                    file.write(line)
#                    file.write('\n')

#            file = open('Passwords.txt', 'w')
#            str1 = repr(password)
#            file.write('\n' + str1 + '\n')
#            file.close
#            f = open('Passwords.txt', 'r')
#            if f .mode == 'r':
#                contents=f.read
#                contents

generate_random_password()
