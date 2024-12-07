import math

with open("Day7.in", "r") as f:
    data = [i for i in f.read().split("\n")]

part_1 = 0
for line in data:
    ans, nums = line.split(":")
    nums = [int(i) for i in nums if i != " "]

    if sum(nums) == ans or math.prod(nums) == ans:
        part_1 += 1
        continue
    elif math.prod(nums) < ans:
        continue
    




            