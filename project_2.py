# Random Password Generator

# password with 8 to 16 digits containing:
# uppercase(A-Z), lowercase(a-z), digits(0-9), special character or punctuation(!, ?, @, #, $, etc)

# Create a List with all the characters -> to generate -> 8 random characters 

import random            # to generate random value 

import string            # give all the chacarters(in string type)

''' string functions :
print(string.ascii_letters)      # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.ascii_lowercase)    # abcdefghijklmnopqrstuvwxyz
print(string.ascii_uppercase)    # ABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)             # 0123456789
print(string.punctuation)        # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

# ASCII - American Standard code for information interchange
# ASCII consist all the characters, and it is having a perticular code for each and every character
# 'A' --> 97(ASCII code)
# 'B' --> 98
# 'C' --> 99
# 'D' --> 100
# ........
'''

# make a variable to store all the string values (using String concatenation)

charVal = string.ascii_letters + string.digits + string.punctuation

# print(random.choice(charVal))     # Give a single random value

# For 8 random values

password = ""   # create a empty string

for i in range(1, 9):          # loop runs 8 times
    password += random.choice(charVal)       # Generated value store in password one bt one

print(password) 

# or

# For 8 random values
pass_len = 8
password = ""   # create a empty string

for i in range(pass_len):          # loop runs 8 times
    password += random.choice(charVal)       # Generated value store in password one bt one

print(password) 


# Create same project using list comprehension

import random
import string

charVal = string.ascii_letters + string.digits + string.punctuation

pass_len = 8     # password lenght

password = ""    # Empty string
password = "".join([random.choice(charVal) for i in range(pass_len)])   # .join([function loop])

# join - concatenate all the string generated in password 
print(password)