#!/usr/bin/env python3
import itertools

names = ['jake', 'melissa', 'oliver', 'emily']
years = ['1987', '1954', '1963']
symbols = ["!","@","#","$","%","&","*","-","=","_","+",".",","]

# loop inside a loop inside a loop for each possible permutation
# aka stupid and ugly code that doesn't scale at all
list1 = [(x + y + z) for x in names for y in years for z in symbols]
list2 = [(x + z + y) for x in names for y in years for z in symbols]
list3 = [(y + x + z) for x in names for y in years for z in symbols]
list4 = [(y + z + x) for x in names for y in years for z in symbols]
list5 = [(z + x + y) for x in names for y in years for z in symbols]
list6 = [(z + y + x) for x in names for y in years for z in symbols]
master_list = list1 + list2 + list3 + list4 + list5 + list6
'''
with open('passwords.txt', 'w') as x:
    for password in master_list:
        # new line for each item in final list
        x.write('%s\n' %password)
'''
# debug list
print(master_list)
