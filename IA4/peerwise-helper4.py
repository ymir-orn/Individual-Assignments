#!/usr/bin/python3

# Author: Ýmir Örn Ingólfsson
# Title : Automation of selecting page numbers in abook
# Note  : use import random. 

import random ,argparse, configparser, os

# -- main code --

# Configparser 
cfg = configparser.ConfigParser()
cfg.read(os.path.expanduser("~/.peerwise.ini"))
verbose = cfg.getboolean("settings","verbose",fallback=False)

# Command line arguments
p = argparse.ArgumentParser()
p.add_argument("--min_page", type=int, default=0) 
p.add_argument("--max_page", type=int, default=100) 
p.add_argument("--num_pages", type=int, default=1) 
args = p.parse_args()

numbers = list(range(args.min_page, args.max_page+1))  # creates a list of numbers in a range from x to y, x<y.
random.shuffle(numbers)                 # randomises the numbers in the list

try:
    for i in range(args.num_pages):     # Loop that prints out the page number
        print(f"page: {numbers[i]}")
    if verbose:
        print(f"(Chosen from pages: {args.min_page}-{args.max_page})")
except:
    print("ERROR:Number out of range!")

# The same page can not be selected twice as there is a finite abmount of pages !
