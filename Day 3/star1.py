#!/usr/bin/python3
import string
same_items = []
priority = []
lazy_count = []

with open("input.txt", "r") as rucksacks:
    for rucksack in rucksacks:
        lazy_count.append("x")
        rucksack = [x for x in rucksack.strip()]
        #print (rucksack)
        compartment_size = int(len(rucksack)/2)
        #print (compartment_size)
        a = rucksack[0:compartment_size]
        b = rucksack[compartment_size:]
        for item in a:
            if item in b:
                same_items.append(item)
                break
print (same_items)
#print ("duplicate items: {}".format(len(same_items)))
#print ("number of rucksacks: {}".format(len(lazy_count)))

lower = [i for i in string.ascii_lowercase]
upper = [i for i in string.ascii_uppercase]

for item in same_items:
    if item in lower:
        priority.append(int(lower.index(item)) + 1)
    elif item in upper:
        priority.append(int(upper.index(item)) + 27)
#print (priority)
print ("Sum of priorities: {}".format(sum(priority)))
