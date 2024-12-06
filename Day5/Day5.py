with open("Day5.in", "r") as f:
    data = [i for i in f.read().split("\n")]

guides = [list(map(int, line.split("|"))) for line in data[:data.index("")]]
updates = [list(map(int, line.split(","))) for line in data[data.index("") + 1:]]
incorrect_updates = []

keys = {}
for key, value in guides:
    if key in keys:
        keys[key].append(value)
    else:
        keys[key] = [value]

def invalid_update(update):
    for i, num in enumerate(update):
        if num in keys:
            for value in keys[num]:
                if value in update and update.index(value) < i:
                    return True
    return False

## PART 1 ##
sum = 0
for update in updates:
    if not(invalid_update(update)):
        sum += update[len(update) // 2]
    else:
        incorrect_updates.append(update)

print(sum)

## PART 2 ##
sum2 = 0
for update in incorrect_updates:
    
    before_nums = {}
    for num in update:
        before_nums[num] = []
        if num in keys:
            for value in keys[num]:
                if value in update: before_nums[num].append(value)  
    
    new_order = []
    while len(before_nums) > 0:

        num_counts = {}
        for num in before_nums:
            num_counts[num] = 0

        for key, val_list in before_nums.items():
            for num in val_list:
                num_counts[num] += 1
                
        for num in num_counts:
            if num_counts[num] == 0:
                new_order.append(num)
                del before_nums[num]

    
    sum2 += new_order[len(update) // 2]

print(sum2)