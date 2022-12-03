#!/usr/bin/python3

rounds = []
results = []
with open("input.txt", "r") as stuff:
    for line in stuff:
        rounds.append(list(line.split(" ")))

#print(rounds)

for round in rounds:
    # Add outcome value
    if (round[0] == "A" and round[1].strip() == "X") or (round[0] == "B" and round[1].strip() == "Y") or (round[0] == "C" and round[1].strip() == "Z"):
       round.append(3)
    elif (round[0] == "A" and round[1].strip() == "Y") or (round[0] == "B" and round[1].strip() == "Z") or (round[0] == "C" and round[1].strip() == "X"):
        round.append(6)
    elif (round[0] == "A" and round[1].strip() == "Z") or (round[0] == "B" and round[1].strip() == "X") or (round[0] == "C" and round[1].strip() == "Y"):
        round.append(0)

for round in rounds:
    # change to value of my chosen item
    if round[1].strip() == "X":
        round[1] = 1
    elif round[1].strip() == "Y":
        round[1] = 2
    elif round[1].strip() == "Z":
        round[1] = 3

for round in rounds:
    # add score for that round to a list
    results.append(sum(round[-2:]))


print (sum(results))
