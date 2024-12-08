def find_start_pos(grid):
    for row_num, row in enumerate(grid):
        if row.find("^") != -1:
            return [row.index("^"), row_num]

def handle_rotation(added_obstacle=[None, None]):
    if y + direction[1] < 0 or x + direction[0] < 0:
        raise IndexError
    elif grid[y + direction[1]][x + direction[0]] == "#" or [x + direction[0], y + direction[1]] == added_obstacle:
        return [-direction[1], direction[0]] # 90 degree rot
    return direction

def is_new_pos(pos, include_dir=False):
    if include_dir:
        pass
    elif pos not in traveled_locs:
        traveled_locs.append(pos)
        return True
    return False

## PART 1 ##
with open("Day6.in", "r") as f:
    grid = [i for i in f.read().split("\n")]

# Get guard location
pos = find_start_pos(grid)

# Initialize position, list, direction
start_pos = pos
traveled_locs = []
traveled_locs.append(start_pos)
direction = [0, -1]

# Tracker variables
sum = 0
in_bounds = True

while in_bounds:
    x, y = pos
    try:
        direction = handle_rotation()

    except IndexError:
        in_bounds = False

    pos = [x + direction[0], y + direction[1]]
    sum += is_new_pos(pos)


print(sum)

## PART 2 ##
orientations = []

sum2 = 0
progress = 0

solutions = []
for r, c in traveled_locs:
    print(f"{progress}/{len(traveled_locs)}")

    # Initialize Variables
    pos = start_pos
    direction = [0, -1]
    orientations.clear()
    in_bounds = True

    while in_bounds:
        orientation = [pos, direction]

        if orientation not in orientations:
            orientations.append(orientation)
        else:
            solutions.append([c, r])
            sum2 += 1
            in_bounds = False

        x, y = pos
        try:
            direction = handle_rotation([c, r])
            

        except IndexError:
            in_bounds = False

        pos = [x + direction[0], y + direction[1]]
    progress += 1

print(sum2)