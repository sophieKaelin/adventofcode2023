import os

print("\n========== INPUT FILE ==========")

input = []

for line in open('inputs/day01.txt'):
    input.append(line.replace("\n",""))

print("Input: " + str(input) + "\n")

print("\n========== Part 1 ==========")

def findNum(l):
    if str.isdigit(l[0]):
        return l[0]
    return findNum(l[1:])

sum = 0
for line in input:
    sum += int(findNum(line) + findNum(line[::-1]))
print(sum)

print("\n========== Part 2 ==========")
def numInString(x):
    for num in spelt:
      if num in x:
          return num
    return ''

spelt = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
numDict = {}
for x in range(9):
    numDict[spelt[x]] = str(x+1)

def findNum2(l, w, reversed):
    wordNum = numInString(w)
    first = l[0]
    if wordNum != '':
        return numDict[wordNum]
    if str.isdigit(first):
        return first
    if not reversed:    
        return findNum2(l[1:], w+first, False)
    return findNum2(l[1:], first+w, True)

sum = 0
for line in input:
    sum += int(
        findNum2(line, '', False)+
        findNum2(line[::-1], '', True))
print(sum)
