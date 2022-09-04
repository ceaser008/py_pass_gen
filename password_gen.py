from string import ascii_lowercase,ascii_uppercase,punctuation,digits
from colorama import Fore
import string
string.punctuation
import random
contents=list(ascii_lowercase+ascii_uppercase+digits+punctuation)
password=[]

length = int(input("len: "))
for i in range(length):
    password.append(random.choice(contents))
random.shuffle(password)
print(''.join(password))
















