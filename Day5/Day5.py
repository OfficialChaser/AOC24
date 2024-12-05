with open("Day5.in", "r") as f:
    data = [i for i in f.read().split("\n")]

guides = []
keys = {}
updates = []

break_found = False
for line in data:
    if line == "":
        break_found = True
    
    elif break_found:
        updates.append(line.split(","))
    else:
        guides.append(line.split("|"))

for guide in guides:
    key = int(guide[0])
    value = int(guide[1])

    if key in keys:
        keys[key].append(value)
    else:
        keys[key] = [value]

incorrect_updates = []

## PART 1 ##
sum = 0
for update in updates:
    order = [int(i) for i in update]
    
    incorrect_update = False
    for i, num in enumerate(order):
        if num in keys:
            for value in keys[num]:
                if value in order and order.index(value) < i:
                    incorrect_update = True
                    incorrect_updates.append(order)
                    break
            
            if incorrect_update:
                break
    
    if not(incorrect_update):
        sum += order[int(len(order) / 2)]

print(sum)

## PART 2 ##
sum2 = 0
for update in incorrect_updates:
    order = [int(i) for i in update]
    
    before_nums = {}
    for num in order:
        before_nums[num] = []

    for num in order:
        if num in keys:
            for value in keys[num]:
                if value in order:
                    before_nums[num].append(value)
    
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

    
    sum2 += new_order[int(len(order) / 2)]

print(sum2)