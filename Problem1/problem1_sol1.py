#!/usr/bin/env python3
import itertools

names = ['jake', 'melissa', 'oliver', 'emily']
years = ['1987', '1954', '1963']
symbols = ["!","@","#","$","%","&","*","-","=","_","+",".",","]

# user input list
a = []
carry_on = ''
stop_list = input('create a custom list? (y/n) ')
if stop_list == 'y':
    while carry_on != 'n' or 'N':
        if stop_list == 'y':
            element = input('add to list: ')
            a.append(element)
            carry_on = input('add more? (y/n) ')
            if carry_on == 'n':
                break
        else:
            break
# debug user input list
#print(a)

# loop inside a loop inside a loop for each possible permutation
'''
list1 = [(x + y + z) for x in names for y in years for z in symbols]
list2 = [(x + z + y) for x in names for y in years for z in symbols]
list3 = [(y + x + z) for x in names for y in years for z in symbols]
list4 = [(y + z + x) for x in names for y in years for z in symbols]
list5 = [(z + x + y) for x in names for y in years for z in symbols]
list6 = [(z + y + x) for x in names for y in years for z in symbols]
list
master_list = list1 + list2 + list3 + list4 + list5 + list6
'''
list_of_lists = [a, names, years, symbols]
final_list = list(itertools.product(a, names, years, symbols))
# final_list = [''.join(str(y) for y in x) for x in itertools.product(a, names, years, symbols)]
# final_list = list(itertools.permutations(list_of_lists))
# create and write to file containing passwords
'''
with open('passwords.txt', 'w') as x:
    for password in final_list:
        # new line for each item in final list
        x.write('%s\n' %password)
'''
# debug list
print(final_list)
