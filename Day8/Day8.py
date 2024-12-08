from itertools import *
with open("Day8.in", "r") as f:
    data = [i for i in f.read().split("\n")]

## PART 1 ##
sum = 0
hashmap = {}
filled_locs = []

for x, line in enumerate(data):
    for y, char in enumerate(line):
        if char == ".":
            continue
        if char not in hashmap:
            hashmap[char] = [[x, y]]
        else:
            hashmap[char].append([x, y])

for char in hashmap:    
    coord_pairs = list(combinations(hashmap[char], 2))
    print(coord_pairs)
    for c1, c2 in coord_pairs:
        c1_x, c1_y = c1
        c2_x, c2_y = c2
        x_diff = abs(c1_x - c2_x)
        y_diff = abs(c1_y - c2_y)

        coord1_x = c1_x + x_diff if c1_x > c2_x else c1_x - x_diff
        coord2_x = c2_x + x_diff if c2_x > c1_x else c2_x - x_diff

        coord1_y = c1_y - y_diff if c1_y < c2_y else c1_y + y_diff
        coord2_y = c2_y - y_diff if c2_y < c1_y else c2_y + y_diff

        coord1 = [coord1_x, coord1_y]
        coord2 = [coord2_x, coord2_y]
        
        if 0 <= coord1[0] < len(data[0]) and 0 <= coord1[1] < len(data) and coord1 not in filled_locs:
            filled_locs.append(coord1)
            sum += 1
        if 0 <= coord2[0] < len(data[0]) and 0 <= coord2[1] < len(data) and coord2 not in filled_locs:
            filled_locs.append(coord2)
            sum += 1
print(sum)

## PART 2 ##
sum2 = 0
filled_locs.clear()
for char in hashmap:    
    coord_pairs = list(combinations(hashmap[char], 2))
    print(coord_pairs)
    for c1, c2 in coord_pairs:
        c1_x, c1_y = c1
        c2_x, c2_y = c2
        x_diff = abs(c1_x - c2_x)
        y_diff = abs(c1_y - c2_y)

        coord1_x = 0
        coord2_x = 0
        coord1_y = 0
        coord2_y = 0
        
        while True:
            keep_going = False
            coord1_x += c1_x + x_diff if c1_x > c2_x else c1_x - x_diff
            coord2_x += c2_x + x_diff if c2_x > c1_x else c2_x - x_diff

            coord1_y += c1_y - y_diff if c1_y < c2_y else c1_y + y_diff
            coord2_y += c2_y - y_diff if c2_y < c1_y else c2_y + y_diff

            coord1 = [coord1_x, coord1_y]
            coord2 = [coord2_x, coord2_y]
            
            if 0 <= coord1[0] < len(data[0]) and 0 <= coord1[1] < len(data) and coord1 not in filled_locs:
                filled_locs.append(coord1)
                sum2 += 1
                keep_going = True
            if 0 <= coord2[0] < len(data[0]) and 0 <= coord2[1] < len(data) and coord2 not in filled_locs:
                filled_locs.append(coord2)
                sum2 += 1
                keep_going = True

            if not(keep_going):
                break

print(sum2)