#!/usr/bin/env python3

def happy_new_year():
# 10
# 9
# ...
# 2
# 1
# Happy New Year!
    i = 10
    while i > 0:
        print(i)
        i -=  1
    print("Happy New Year!")

def square_integers(int_list):
# [1, 4, 9, 16, 25]
    # int_list = [1, 2, 3, 4, 5]
    # for list in int_list:
    #     square_integers = list ^ 2
    return [num ** 2 for num in int_list]




def fizzbuzz():
#prints the numbers from 1 to 100. For multiples
    #of three, print "Fizz" instead of the number and 
    #for the multiples of five print "Buzz". 
    for i in range(1, 101):
        if i % 3 == 0:
            print("Fizz", end="")
        if i % 5 == 0:
            print("Buzz", end="")
        if i % 3 != 0 and i % 5 != 0:
            print(i, end="")
        print()