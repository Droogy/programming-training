#!/usr/bin/env python3
import itertools
import sys
from config import *

# check if we have cmd line args
if len(sys.argv) > 1:
    # check that custom(-c) flag is set
    if sys.argv[1] == '-c':
        # size of list is 2nd cmd line arg
        list_size = int(sys.argv[2])
        for i in range(list_size):
            element = input('add to list: ')
            a.append(element)

master_pass = []
# permy does all the heavy lifting
def permy(single):
    # itertools magic to iterate over combinations
    list_iterator = list(itertools.product(*single))
    # join together tuple elements to form a password
    final_list = [''.join(tups) for tups in list_iterator]
    # add each password to a master list
    for i in final_list:
        master_pass.append(i)

# at this point, each list is initialized as tuples
# res changes the position of each list in the list of lists
res = itertools.permutations(list_of_lists)

# this loops over each permutation and runs permy against it which 
# generates our passwords 
for x in res:
    permy(x)

# write passwords to file we can use
with open('all_passwords.txt', 'w') as x:
    for password in master_pass:
        x.write(f'{password}\n')

# debug master list
#for x in master_pass:
#    print(x)