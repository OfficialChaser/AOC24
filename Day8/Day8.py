from itertools import *
with open("Day8.in", "r") as f:
    data = [i for i in f.read().split("\n")]

def check_valid(coord):
    if 0 <= coord[0] < len(data[0]) and 0 <= coord[1] < len(data) and coord not in filled_locs:
        filled_locs.append(coord)
        return True
    return False

def calc_slope(x1, y1, x2, y2):
    return [y2 - y1, x2 - x1]

def visualize():
    print(c1, c2)
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            if [x, y] == c1 or [x, y] == c2:
                print("O", end="")
            elif [x, y] in hashmap["0"] or [x, y] in hashmap["A"]:
                print("a", end="")
            if [x, y] in filled_locs:
                print("#", end="")
            else:
                print(".", end="")
        print()
    print()
    

## PART 1 ##
sum = 0
hashmap = {}
filled_locs = []

for y, line in enumerate(data):
    for x, char in enumerate(line):
        if char == ".":
            continue
        if char not in hashmap:
            hashmap[char] = [[x, y]]
        else:
            hashmap[char].append([x, y])

for char in hashmap:    
    coord_pairs = list(combinations(hashmap[char], 2))

    for c1, c2 in coord_pairs:
        c1_x, c1_y = c1
        c2_x, c2_y = c2
        rise, run = calc_slope(c1_x, c1_y, c2_x, c2_y)

        if c1_x < c2_x and c1_y < c2_y:
            rise = -rise

        coord1 = 0
        coord2 = 0

        if c1_x > c2_x:
            coord1 = [c1_x + abs(run), c1_y - rise]
            coord2 = [c2_x - abs(run), c2_y + rise]
        else:
            coord1 = [c2_x + abs(run), c2_y - rise]
            coord2 = [c1_x - abs(run), c1_y + rise]
        
        sum += check_valid(coord1)
        sum += check_valid(coord2)

print(sum)

## PART 2 ##
sum2 = 0
filled_locs.clear()
coord_pairs.clear()
print(hashmap)
for char in hashmap:    
    coord_pairs = list(combinations(hashmap[char], 2))
    for c1, c2 in coord_pairs:
        print(c1, c2)
        print()
        c1 = list(c1)
        c2 = list(c2)
        c1_x, c1_y = c1
        c2_x, c2_y = c2

        rise, run = calc_slope(c1_x, c1_y, c2_x, c2_y)

        if c1_x < c2_x and c1_y < c2_y:
            rise = -rise

        coord1 = c1
        coord2 = c2
        
        finding_coords = True
        new_coords = 0
        while finding_coords:
            print(f"Two points: {coord1, coord2}.")
            prev_sum = sum2

            if c1_x > c2_x:
                coord1[0] += abs(run) 
                coord1[1] -= rise
                coord2[0] -= abs(run) 
                coord2[1] += rise
            else:
                coord2[0] += abs(run) 
                coord2[1] -= rise
                coord1[0] -= abs(run) 
                coord1[1] += rise
            
            sum2 += check_valid(list(coord1))
            sum2 += check_valid(list(coord2))
            
            print(f"New points: {coord1}, {coord2}. Total new coords found: {sum2 - prev_sum}")
            if sum2 == prev_sum:
                finding_coords = False 
            else:
                if c1 not in filled_locs:
                    filled_locs.append(c1)
                    sum2 += 1
                if c2 not in filled_locs:
                    filled_locs.append(c2)
                    sum2 += 1
        
        print()
visualize()
print(sum2)