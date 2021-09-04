import random

print("This is a dice simulator")
x = "y"

while x == "y" :
    num = random.randint(1, 6)
    x = input("roll the dice (y/n) : ")
    if num == 1 :
        print("---------")
        print("|       |")
        print("|   O   |")
        print("|       |")
        print("---------")
    if num == 2 :
        print("---------")
        print("|       |")
        print("| O   O |")
        print("|       |")
        print("---------")
    if num == 3 :
        print("---------")
        print("|   O   |")
        print("|   O   |")
        print("|   O   |")
        print("---------")
    if num == 4 :
        print("---------")
        print("| O   O |")
        print("|       |")
        print("| O   O |")
        print("---------")
    if num == 5 :
        print("---------")
        print("| O   O |")
        print("|   O   |")
        print("| O   O |")
        print("---------")
    if num == 6 :
        print("---------")
        print("| O   O |")
        print("| O   O |")
        print("| O   O |")
        print("---------")
