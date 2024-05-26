import random
import string

print(string.ascii_letters)     # prints mix of capital and small letters
print(string.digits)            # prints numbers from 0 to 9

print(random.choice(string.ascii_letters))      # select any ransom letter
print(random.choice(string.digits))             # select any ransom number


# create a random string of 8 digit length

email = []

for i in range(8):
    email.append(random.choice(string.ascii_letters+string.digits))

print("".join(email))


