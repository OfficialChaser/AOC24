def get_data():
    with open("Day3.in", "r") as f:
        txt = [i for i in f.read().split("\n")]
        data = ""
        for line in txt:
            data += line
    return data

def get_index_msg(i, data):
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

def modify_data(data):
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

    nums = get_index_msg(index, data)
    if nums:
        a, b = list(map(int, nums.split()))
        print(f"{a},{b}")
        sum += a * b

    data = modify_data(data)

print(sum)

