#!/usr/bin/python3

# author: ýmir örn ingólfsson
# Title : automation of repetative task
# note  : use import random.

import random

numbers = list(range(56, 110))  # rpi pages : 56, 110 . pro git pages: 26, 61
random.shuffle(numbers) # creates a list 

for i in 1,2:
    print(numbers[i])
