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
winsPerCard = {}
for i, game in enumerate(input):
    wins = 0
    for winner in game[0]:
        if winner in game[1]:
            wins += 1
    if wins > 0:
        sum += pow(2, wins-1)
    winsPerCard[i+1] = wins

print(sum)

print("\n========== Part 2 ==========")
cardsToCheck = list(range(1,len(input)+1))
# sum2 = 0
idx = 0
while idx < len(cardsToCheck):
    card = cardsToCheck[idx]
    cardsToCheck = cardsToCheck + list(range(card+1, card+1+winsPerCard[card]))
    idx += 1

print(len(cardsToCheck))