import re

print("\n========== INPUT FILE ==========")

input = []

for line in open('inputs/day04.txt'):
    temp = re.split(r':|\|', line.replace("\n",""))
    wins = list(filter(lambda a: a != '', temp[1].split(" ")))
    nums = list(filter(lambda a: a != '', temp[2].split(" ")))
    input.append([wins, nums])

# Format= [[winning numbers, your numbers]]
print("Input: " + str(input) + "\n")

print("\n========== Part 1 ==========")
sum = 0
for game in input:
    wins = 0
    for winner in game[0]:
        if winner in game[1]:
            wins += 1
    if wins > 0:
        sum += pow(2, wins-1)

print(sum)