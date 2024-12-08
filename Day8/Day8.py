from itertools import *
with open("Day8.in", "r") as f:
    data = [i for i in f.read().split("\n")]

sum = 0

hashmap = {}

for y, line in enumerate(data):
    for x, char in enumerate(line):
        if char == ".":
            continue
        if char not in hashmap:
            hashmap[char] = [[x, y]]
        else:
            hashmap[char].append([x, y])
        
print(hashmap)

for char in hashmap:    
    coord_pairs = [''.join(p) for p in product(hashmap[char], r=2)]
    for c1, c2 in coord_pairs:
        pass

print(sum)