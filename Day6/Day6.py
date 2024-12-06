with open("Day6.in", "r") as f:
    grid = [i for i in f.read().split("\n")]

pos = []

for row_num, row in enumerate(grid):
    if row.find("^") != -1:
        pos = [row.index("^"), row_num]

start_pos = pos

## PART 1 ##
in_bounds = True
direction = [0, -1]
traveled_locs = []
unique_locs_traveled = 0
traveled_locs.append(start_pos)
'''
while in_bounds:
    x = pos[0]
    y = pos[1]
    print(pos)
    try:
        print(grid[y + direction[1]][x + direction[0]])
        if grid[y + direction[1]][x + direction[0]] == "#":
            direction = [-direction[1], direction[0]] # 90 degree rot
            continue

    except IndexError:
        in_bounds = False
    
    pos = [x + direction[0], y + direction[1]]
    if pos not in traveled_locs:
        traveled_locs.append(pos)
        unique_locs_traveled += 1

print(unique_locs_traveled)'''


## PART 2 ##
solutions = 0
visited_states = []
for r, row in enumerate(grid):
    print(f"Started row: {r}")
    for c, char in enumerate(row):
        with open("Day6.in", "r") as f:
            grid = [i for i in f.read().split("\n")]
        if char == "#":
            continue
        else:
            steps_taken = 0
            pos = start_pos
            direction = [0, -1]
            grid[r] = grid[r][:c] + "#" + grid[r][c + 1:]
            visited_states.clear()
            looped = False
        while True:
            x = pos[0]
            y = pos[1]

            try:
                if grid[y + direction[1]][x + direction[0]] == "#":
                    direction = [-direction[1], direction[0]]
                    continue

            except IndexError:
                break
            
            pos = [x + direction[0], y + direction[1]]
            steps_taken += 1
            if [pos, direction] not in visited_states:
                visited_states.append([pos, direction])
            else:
                solutions += 1
                break
            
            if steps_taken >= 10000:
                break
                
            
print(solutions)