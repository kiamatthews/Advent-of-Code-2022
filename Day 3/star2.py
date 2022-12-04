#!/usr/bin/python3
import string

stuff = []
badges = []
priority = []


with open("input.txt", "r") as rucksacks:
    for rucksack in rucksacks:
        stuff.append([x for x in rucksack.strip()])

#print (stuff)
groups = [stuff[i:i + 3] for i in range(0, len(stuff), 3)]

print (len(groups))

for group in groups:
   for item in group[0]:
       if item in group[1] and item in group[2]:
           badges.append(item)
           break

print(badges)
lower = [y for y in string.ascii_lowercase]
upper = [y for y in string.ascii_uppercase]

for badge in badges:
    if badge in lower:
        priority.append(int(lower.index(badge)) + 1)
    elif badge in upper:
        priority.append(int(upper.index(badge)) + 27)
#print (priority)
print ("Sum of priorities: {}".format(sum(priority)))
cd