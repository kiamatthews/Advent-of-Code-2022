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

#print (full_pairs)

ordered_pairs = []

for pair in full_pairs:
    ordered_pairs.append(sorted(pair, key=len))
 #   derp_convert = [str(x) for x in derp[1]]

  #  if (str(derp[0][0]) not in derp_convert):
  #      full_pairs.remove(pair)

#print (ordered_pairs)
final_count = []
for pair in ordered_pairs:
    if (pair[0][0] in pair[1]) and pair[0][-1] in pair[1]:
        final_count.append("q")

print ("There are {} pairs where one range fully contains the other".format(len(final_count)))

