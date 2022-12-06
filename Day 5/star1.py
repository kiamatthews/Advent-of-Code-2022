#!/usr/bin/python3

input = ["BWN", "LZSPTDMB", "QHZWR", "WDVJZR", "SHMB", "LGNJHVPB", "JQZFHDLS", "WSFJGQB", "ZWMSCDJ"]
stacks = []

for y in input:
    stacks.append(list(y))

#print (stacks)

instructions = []

with open("input.txt", "r") as data:
    for x in data:
        instructions.append(list(x.strip().split(" ")))

for i in instructions:
    i.remove("move")
    i.remove("from")
    i.remove("to")


for y in instructions:
    f = int(y[1])-1
    to = int(y[2])-1
    print ("Instructions: move {} from stack {} to stack {}".format(y[0], y[1], y[2]))
    print ("From stack is {}".format(stacks[f]))
    print("To stack is {}".format(stacks[to]))
    sub = stacks[f][-int(y[0]):]
    stacks[f] = stacks[f][:-int(y[0])]
    #sub.reverse()
    #print (sub)
    stacks[to].extend(sub)
    print ("New to stack is {}".format(stacks[to]))
    print ("new from stack is {}".format(stacks[f]))

print (stacks)

top =[]
for stack in stacks:
    top.append(stack[-1])
print ("The crates on top of each stack are: " + ''.join(top))










#print (instructions)
