#!/usr/bin/env python3

#Scenario
#---------
#I forgot a WinRAR-archive password.
#I remember there was a name of someone from my (hypothetical) family: jake, melissa, oliver, emily.
#I remember there was a year of birth of someone from my family: 1987, 1954, 1963.
#I remember there was a symbol (that are so recommended by everyone):
#["!","@","#","$","%","&","*","-","=","_","+",".",","]
#But I do not remember an order of these elements.
#You have to find a list of all possible passwords, based on this information.
#There are ~936 of them.

names = ['jake', 'melissa', 'oliver', 'emily']
years = ['1987', '1954', '1963']
symbols = ["!","@","#","$","%","&","*","-","=","_","+",".",","]

# loop inside a loop inside a loop for each possible permutation
list1 = [(x + y + z) for x in names for y in years for z in symbols]
list2 = [(x + z + y) for x in names for y in years for z in symbols]
list3 = [(y + x + z) for x in names for y in years for z in symbols]
list4 = [(y + z + x) for x in names for y in years for z in symbols]
list5 = [(z + x + y) for x in names for y in years for z in symbols]
list6 = [(z + y + x) for x in names for y in years for z in symbols]

master_list = list1 + list2 + list3 + list4 + list5 + list6
# create and write to file containing passwords
with open('passwords.txt', 'w') as x:
    for password in master_list:
        # new line for each item in master list
        x.write('%s\n' %password)
# debug list
# print(master_list)