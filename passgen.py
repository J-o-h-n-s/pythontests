import random
import numpy as np
from contextlib import redirect_stdout

print('Hey, bitch')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#¤%&/()@£$€.,-''"¨1234567890'
number = input('Amount of passwords: ')
lengt = input('Length of passwords: ')
number = int(number)
lengt = int(lengt)

print('Following passowrds saved in passwords.txt:')

for pwd in range(number):
    passwords = ''
    for c in range (lengt):
        passwords += random.choice(chars)
    print(passwords)

with open('Passwords.txt', 'w') as f:
    with redirect_stdout(f):
        print(passwords)





#np.savetxt('Passowrds.txt', passwords)
#print(open('Passwords.txt').read)

#with open('Passwords.txt', 'w') as p:
#    for loi in passwords:
#        p.writelines(loi)
#        p.write('\n')

#    p.write(passwords)
