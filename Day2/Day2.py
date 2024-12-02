with open("Day2.in", "r") as f:
    data = [i for i in f.readlines()]

def is_safe(nums):
    decreasing = nums[0] > nums[1]
    add_to_sum = True
    for i in range(len(nums) - 1):
        diff = abs(nums[i] - nums[i+1])
        if not(0 < diff <= 3):
            add_to_sum = False
        if decreasing and nums[i] < nums[i+1]:
            add_to_sum = False
        if not decreasing and nums[i] > nums[i+1]:
            add_to_sum = False
    
    return add_to_sum
    
    

## PART 1 ##
sum = 0
for line in data:
    nums = [int(i) for i in line.split()]
    
    if is_safe(nums):
        sum += 1
        
print(sum)

## PART 2 ##
sum2 = 0
for line in data:
    nums = [int(i) for i in line.split()]

    for i in range(len(nums)):
        
        temp_nums = []
        for j, num in enumerate(nums):
            if i == j:
                continue
            else:
                temp_nums.append(num)
        
        if is_safe(temp_nums):
            sum2 += 1
            break
        else:
            pass

print(sum2)