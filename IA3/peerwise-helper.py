#!/usr/bin/python3

# Author: Ýmir Örn Ingólfsson
# Title : Automation of selecting page numbers in abook
# Note  : use import random. 

import random

# main code

numbers1 = list(range(114, 156+1))  # creates a list of numbers in a range from x to y, x<y.
numbers2 = list(range(208,216+1))
numbers = numbers1+numbers2         # combines the 2 lists into 1 list.
random.shuffle(numbers)             # randomises the numbers in the list
number_of_pages = int(input("Enter number of questions: ")) # input for arbritary number of page numbers

try:
    for i in range(number_of_pages): # Loop that prints out the page number
        print(numbers[i])
except:
    print("ERROR:Number out of range!")

# The same page can not be selected twice as there is a finite abmount of pages !
