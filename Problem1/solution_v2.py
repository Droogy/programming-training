#!/usr/bin/env python3
import itertools
import sys

names = ['jake', 'melissa', 'oliver', 'emily']
years = ['1987', '1954', '1963']
symbols = ['!','@','#','$','%','&','*','-','=','_','+','.',',']


# user input list
a = []
# check if we have cmd line args
if len(sys.argv) > 1:
    # check that custom(-c) flag is set
    if sys.argv[1] == '-c':
        # size of list is 2nd cmd line arg
        list_size = int(sys.argv[2])
        for i in range(list_size):
            element = input('add to list: ')
            a.append(element)
else:
    pass
# debug user input list
print("user list is: " +str(a))

# debug user list
#a = ['aaa', 'bbb', 'ccc']

# initialize all the lists
list_of_lists = [a, names, years, symbols]
# iterate over each list element, but in place, not the permutation we need
list_iterator = list(itertools.product(*list_of_lists))
# join together the tuples into one string
final_list = [''.join(tups) for tups in list_iterator]

# print passwords to file
with open('passwords.txt', 'w') as x:
    for password in final_list:
        # new line for each item in final list
        x.write('%s\n' %password)

# debug list
print(final_list)
