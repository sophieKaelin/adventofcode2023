import re
import math

print("\n========== INPUT FILE ==========")

input, idx = [], 0

for line in open('inputs/day02.txt'):
    temp = re.split(r';|,|:', line.replace("\n",""))
    input.append([temp[0].lstrip("Game ")]) # Add game number to list
    for t in temp[1:]:
        input[idx].append(t.strip().split(" ")) # Add game values to list
    idx+=1

# Format: [GameNumber, [#, colour], [#, colour]...]
print("Input: " + str(input) + "\n")

print("\n========== Part 1 ==========")

sumTotal, invalid = 0,0
maxVals = {"red":12, "green":13, "blue":14}
for line in input:
    gameID = int(line[0])
    sumTotal += gameID
    for item in line[1:]:
        num, colour = int(item[0]), item[1]
        if num > maxVals[colour]:
            invalid += gameID
            break
print(sumTotal-invalid)

print("\n========== Part 2 ==========")
sum2 = 0
for line in input:
    maxVals = {"red": 0, "green":0, "blue":0}
    for item in line[1:]:
        num, colour = int(item[0]), item[1]
        maxVals[colour] = max(num, maxVals[colour])
    sum2 += math.prod(maxVals.values())
print(sum2)
