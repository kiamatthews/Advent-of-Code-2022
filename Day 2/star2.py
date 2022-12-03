#!/usr/bin/python3

rounds = []
results = []
with open("input.txt", "r") as stuff:
    for line in stuff:
        rounds.append(list(line.split(" ")))

for round in rounds:
    # change to value chosen item
    if round[0].strip() == "A":
        round[0] = 1
    elif round[0].strip() == "B":
        round[0] = 2
    elif round[0].strip() == "C":
        round[0] = 3

for round in rounds:
    round[1] = round[1].strip()
    # draw
    if round[1] == "Y":
        round.append(3)
        round[1] = round[0]
        results.append(sum(round[-2:]))
    # losses
    elif round[1] == "X" and round[0] == 1:
        round.append(0)
        round[1] = 3
        results.append(sum(round[-2:]))
    elif round[1] == "X" and round[0] == 2:
        round.append(0)
        round[1] = 1
        results.append(sum(round[-2:]))
    elif round[1] == "X" and round[0] == 3:
        round.append(0)
        round[1] = 2
        results.append(sum(round[-2:]))
    # wins
    elif round[1] == "Z" and round[0] == 1:
        round.append(6)
        round[1] = 2
        results.append(sum(round[-2:]))
    elif round[1] == "Z" and round[0] == 2:
        round.append(6)
        round[1] = 3
        results.append(sum(round[-2:]))
    elif round[1] == "Z" and round[0] == 3:
        round.append(6)
        round[1] = 1
        results.append(sum(round[-2:]))


print(sum(results))