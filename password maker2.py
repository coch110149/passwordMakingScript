"""
A program to produce a randomly generatored strong password
"""

import random
import string

def makePassword():

    passwordLength = random.randint(15,50)
    password = ""
    charList = string.printable
    for index in range (passwordLength):
        char = charList[random.randint(0,94)]
        password += char
    return password

def writeToFile(password):
    file = open("Open me for a secure password.txt", "w")
    file.write("Copy the password below and paste it in a password field\n")
    file.write("\n"+ password)
    file.close()
    
def main ():
    password = makePassword()
    print
    writeToFile(password)
main()


             




