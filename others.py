import os
name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")

if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")

pingName = input('What is the org you wanna search for?\n')
os.system("ping -n 5 %s.org" %pingName)
tupin = input('What info do you wanna search for?\n')
os.system("%s tupin" %tupin)