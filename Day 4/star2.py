#!/usr/bin/python3

pairs =[]

with open("input.txt", "r") as data:
    for x in data:
        pairs.append(list(x.strip().split(",")))

#print (pairs)

pairs_extended = []
for pair in pairs:
    for elf in pair:
        pairs_extended.append(list(elf.split("-")))

pairs_extended = [pairs_extended[i:i + 2] for i in range(0, len(pairs_extended), 2)]

#print (pairs_extended)

full_pairs = []
for pair in pairs_extended:
    for elf in pair:
        full_pairs.append(list(range(int(elf[0]), int(elf[1]) + 1)))

full_pairs = [full_pairs[i:i + 2] for i in range(0, len(full_pairs), 2)]

print (full_pairs)

derp = []
for pair in full_pairs:
    for item in pair[0]:
        if item in pair[1]:
            derp.append("yes{}".format(item))
            break


print (derp)
print ("There are {} pairs where there is any overlap at all".format(len(derp)))
