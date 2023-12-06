
print("\n========== INPUT FILE ==========")

input = []

for line in open('inputs/day03.txt'):
    input.append(line.replace("\n",""))

print("Input: " + str(input) + "\n")

print("\n========== Part 1 ==========")

def isSymbol(val):
    return not (val.isdigit() or val == ".")


def createNum(r, c1, c2):
    return int(''.join(input[r][c1:c2+1]))


def getIdxToCheck(r, c1, c2):
    coords = []
    # Top
    if r-1 >= 0:
        for x in range(c1-1, c2+2):
            if x <= -1 or x >= maxC:
                continue
            coords.append([r-1, x])        
    # Below
    if r+1 < maxR:
        for x in range(c1-1, c2+2):
            if x <= -1 or x >= maxC:
                continue
            coords.append([r+1, x])     
    # Left
    if c1-1 >= 0:
        coords.append([r, c1-1])
    # Right
    if c2+1 < maxC:
        coords.append([r, c2+1])
    return coords

def hasAdjacentSymbols(row, cols):
    for coords in getIdxToCheck(row, cols[0], cols[-1]):
        if isSymbol(input[coords[0]][coords[1]]):
            return True
    return False

part = 0
maxC, maxR = len(input[0]), len(input)

for idxR, row in enumerate(input):
    cols = [] 
    for idxC, col in enumerate(row):
        if col.isdigit():
            cols.append(idxC)
        if idxC == len(row)-1 or not col.isdigit():
            if len(cols) == 0:
                continue
            if hasAdjacentSymbols(idxR, cols):
                part += createNum(idxR, cols[0], cols[-1])
                cols = []
                continue
            cols = []
            continue
        
print(part==525911)

print("\n========== Part 2 ==========")

gears = []
gearDict = {}
for rowIdx, i in enumerate(input):
    s = 0
    while i.find("*", s) != -1:
        cIdx = i.find("*", s)
        gears.append([rowIdx, cIdx])
        gearDict[",".join([str(rowIdx), str(cIdx)])] = []
        s = cIdx+1

part2 = 0
for idxR, row in enumerate(input):
    cols = [] 
    for idxC, col in enumerate(row):
        if col.isdigit():
            cols.append(idxC)
        if idxC == len(row)-1 or not col.isdigit():
            print(cols)
            print(len(cols) == 0)
            if len(cols) == 0:
                continue
            print(cols)
            for i in getIdxToCheck(idxR, cols[0], cols[-1]):
                if i in gears:
                    # Why is cols empty here?
                    print(cols)
                    gearDict[",".join([str(i[0]),str(i[1])])].append(createNum(idxR, cols[0], cols[-1]))
                cols = []
                continue
            cols = []
            continue
print(gearDict)
        
print(part2)