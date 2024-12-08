import math
import time
from itertools import *

start_time = time.time()

def parse_data(line):
    ans, nums = line.split(": ")
    ans = int(ans)
    nums = [int(i) for i in nums.split(" ")]
    return ans, nums

with open("Day7.in", "r") as f:
    data = [i for i in f.read().split("\n")]

## PART 1 ##
part_1 = 0
for line in data:
    ans, nums = parse_data(line)

    if sum(nums) == ans or math.prod(nums) == ans:
        part_1 += ans
        continue
    
    sign_orders = [''.join(p) for p in product("*+", repeat=len(nums) - 1)]
    
    for i in range(len(sign_orders)):
        result = nums[0]
        for j in range(len(nums) - 1):
            if sign_orders[i][j] == "*":
                result *= nums[j + 1]
            else:
                result += nums[j + 1]
            
        if result == ans:
            part_1 += ans
            break

print(f"Part 1: {part_1}")
print(f"Time elapsed for part 1: {round(time.time() - start_time, 2)}s")

## PART 2 ##
start_time = time.time()
part_2 = 0

for line in data:
    ans, nums = parse_data(line)
    if sum(nums) == ans or math.prod(nums) == ans:
        part_2 += ans
        continue
    
    sign_orders = [''.join(p) for p in product("*+|", repeat=len(nums) - 1)]
    
    for i in range(len(sign_orders)):
        result = nums[0]
        for j in range(len(nums) - 1):
            if sign_orders[i][j] == "*":
                result *= nums[j + 1]
            elif sign_orders[i][j] == "|":
                str_result = str(result)
                str_result += str(nums[j + 1])
                result = int(str_result)
            else:
                result += nums[j + 1]
            
        if result == ans:
            part_2 += ans
            break

print(f"Part 2: {part_2}")
print(f"Time elapsed for part 2: {round(time.time() - start_time, 2)}s")
            