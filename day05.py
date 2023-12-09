import sys
print("\n========== INPUT FILE ==========")

class Seed:
  def __init__(self, seed):
    self.vals = [seed,-1,-1,-1,-1,-1,-1,-1]
  # 0 = seed, 1 = soil, 2 = fertilizer, 3 = water, 4 = light, 5 = temp, 6 = humidity, 7 = loc
  vals = []

seeds = []
keyPhrase = {}

kpIDX = ''
for line in open('inputs/day05.txt'):
    line = line.replace("\n","")
    if line == "":
        continue
    elif "seeds:" in line:
        seeds = [Seed(eval(i)) for i in line.split(": ")[1].split(" ")]
        keyPhrase[line.split(" ")[0]] = [eval(i) for i in line.split(" ")[1:]]
    elif "map" in line:
        keyPhrase[line] = []
        kpIDX = line
    else:
        keyPhrase[kpIDX].append([eval(i) for i in line.split(" ")])

print("Input: " + str(keyPhrase) + "\n")

print("\n========== Part 1 ==========")

for i, map in enumerate(keyPhrase.keys()):
   if i == 0:
      continue
   for mapVals in keyPhrase[map]:
      destStart, sourceStart, rangeLen = mapVals
      for seed in seeds:
         # Set current value to previous by default, and update only if there is a mapping range.
         if seed.vals[i] == -1:
            seed.vals[i] = seed.vals[i-1]
         elif seed.vals[i-1] >= sourceStart and seed.vals[i-1] < sourceStart + rangeLen:
            seed.vals[i] = destStart + (seed.vals[i-1] - sourceStart)

# Find the lowest location
lowest = sys.maxsize
for seed in seeds:
   lowest = min(lowest, seed.vals[-1])
print(lowest==51752125)