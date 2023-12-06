print("\n========== INPUT FILE ==========")

class Seed:
  def __init__(seed):
    self.val = seed
  val = -1
  soil = -1
  fertilizer = -1
  water = -1
  light = -1
  temp = -1
  humidity = -1
  loc = -1


keyPhrase = {
    "seeds: ":[],
    "seed-to-soil map:":[], 
    "soil-to-fertilizer map:":[], 
    "fertilizer-to-water map:":[], 
    "water-to-light map:":[], 
    "light-to-temperature map:":[], 
    "temperature-to-humidity map:":[], 
    "humidity-to-location map:":[]}
kpIDX = ''
for line in open('inputs/day05.txt'):
    line = line.replace("\n","")
    if line == "":
        continue
    elif "seeds:" in line:
        # TODO -> convert seeds into seed objects. Maybe just do this later?
        keyPhrase["seeds: "] = [eval(i) for i in line.split(": ")[1].split(" ")]
        continue
    elif "map" in line:
        kpIDX = line
        continue
    keyPhrase[kpIDX].append([eval(i) for i in line.split(" ")])

print("Input: " + str(keyPhrase) + "\n")

print("\n========== Part 1 ==========")