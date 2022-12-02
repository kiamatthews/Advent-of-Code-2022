#!/usr/bin/python3

from itertools import groupby

inventory = []
total_cals = []
elf_list = []
with open("input.txt", "r") as f_in:
    for v, g in groupby(f_in, lambda k: k.startswith('\n')):
        if not v:
            inventory.append(list(map(str.strip, g)))

#print(inventory)

for elf in inventory:
    elf = list(map(int, elf))
    total_cals.append(sum(elf))



print ("First star: {}".format(sorted(total_cals)[-1]))

most = sorted(total_cals)[-3:]
print ("Second star: {}".format(sum(most)))


