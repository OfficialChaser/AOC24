def get_data():
    with open("Day3.in", "r") as f:
        txt = [i for i in f.read().split("\n")]
        data = ""
        for line in txt:
            data += line
    return data

def get_index_msg(i):
    j = 1
    nums = ""
    while True:
        current_char = data[i + j]
        if current_char.isnumeric():
            nums += current_char
        elif current_char == ",":
            nums += " "
        elif current_char == ")" and " " in nums:
            return nums
        else:
            return ""
        j += 1

def modify_data(index):
    indexes_to_remove = []
    for j in range(3):
        indexes_to_remove.append(index + j)

    new_data = ""
    for i, char in enumerate(data):
        if i >= indexes_to_remove[-1]:
            new_data += char
    return new_data


## PART 1 ##
data = get_data()

sum = 0
while True:
    index = data.find("mul(")
    if index == -1:
        break

    index += 3

    nums = get_index_msg(index)
    if nums:
        a, b = list(map(int, nums.split()))
        sum += a * b

    data = modify_data(index)

print(sum)


## PART 2 ##
data = get_data()
sum2 = 0
enabled = True

while True:
    mul_index = data.find("mul(")
    if mul_index == -1:
        break

    do_index = data.find("do()")
    dont_index = data.find("don't()")
    
    if dont_index < mul_index and dont_index != -1:
        enabled = False
    elif do_index < mul_index and do_index != -1:
        enabled = True

    mul_index += 3

    nums = get_index_msg(mul_index)
    if nums and enabled:
        a, b = list(map(int, nums.split()))
        sum2 += a * b

    data = modify_data(mul_index)

print(sum2)