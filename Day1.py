with open("Day1.in", "r") as f:
    data = [i for i in f.readlines()]

## PART 1 ##
left_nums = []
right_nums = []

for line in data:
    left, right = [int(i) for i in line.split()]
    left_nums.append(left)
    right_nums.append(right)

left_nums.sort()
right_nums.sort()

sum = 0
for left, right in zip(left_nums, right_nums):
    sum += abs(left - right)

print(sum)

## PART 2 ##
sum2 = 0
for num in left_nums:
    sum2 += right_nums.count(num) * num

print(sum2)