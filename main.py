from dices import *
from random import randint
import sys


def generate_row(value=1):

    total = 0
        

    for i in range(int(value)):
        num = randint(1, 6)
        print(dices[num], end="")
        total += num

    return f"Total: {total}"




try:
    value = int(input("Type value of dices (1 - 6): "))

    if value < 1 and value > 6:
        print("encorect number of dices (1 - 6)")
    else: 
        print(generate_row(value))
except:
    print(generate_row())
    