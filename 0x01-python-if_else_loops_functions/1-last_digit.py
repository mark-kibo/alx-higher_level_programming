#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n=str(number)
if n[-1] == '0':
    print("Last digit of {:d} is {:s} and is 0".format(number, n[-1]))
elif n[-1] < '6' and n[-1] != '0':
    print("Last digit of {:d} is {:s} and is less than 6 and not 0".format(number,n[-1]))
elif n[-1] > '5':
    print("Last digit of {:d} is {:s} and is greater than 5".format(number, n[-1]))
