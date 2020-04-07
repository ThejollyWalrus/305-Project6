# Mason Hamilton & Dylan Nasser
# CST-305-1:55
# Professor Ricardo Citro
# 4/5/20
# Project 6 Taylor Polynomials
# Colobrated with Ryan and Michael and logan and blake for help

#import libaries below
import sympy as sy
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from sympy.functions import sin, cos
import math
from sympy import *
import time
steps = 0

#part 2 fucntion to print the general solution
def part2():
    start = time.time()
    global steps
    a = [1, 1]

    i = 0.0
    #createing the range for first a0 equation
    for x in range(0, 9):
        a.append(round((i ** 2 - i + 1) / (4 * (i + 2) * (i + 1)) * a[x], 4))
        i += 1

    print("y = ")
    #big if or elif statment printing the correct values
    for x in range(0, len(a)):
        if (x == 0):
            print("a0 +")
            steps += 1
        elif (x == 1):
            print("a_1x +")
            steps += 1
        elif (x % 2) == 0:
            print(str(a[x]) + " * a_0x^" + str(x) + " +")
            steps += 1
        elif (x % 2) != 0:
            print(str(a[x]) + " * a_1x^" + str(x) + " +")
            steps += 1
    print(")")


    print("\n")
    #the function to print the second fucntion
    print("y = a_0 (")
    for x in range(0, len(a)):
        if (x % 2) == 0:
            print(str(a[x]) + "x^" + str(x) + " +")
            steps += 1


    print(") + a_1 (")
    for x in range(0, len(a)):
        if (x % 2) != 0:
            print(str(a[x]) + "x^" + str(x) + " +")
            steps += 1
    print(")")

    end = time.time()
    print("It took this many seconds: ", end - start)



#Calling the part 2 function
print("\n")
part2()




print("Steps: ", steps)