#This program generates a Random Password
import random
import string

print("Welcome to the Random passwrod generator")

charlen = int(input("how much Digits of Random password you want: ")) 

char = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

rand_passwd = random.choice(char)

password = ""
for i in range(charlen):
    password += random.choice(char)
    
def get_password():
    print(f"Here is your password: \n{password}")

get_password()

print("Program Created by STARK \nTHANK YOU.")