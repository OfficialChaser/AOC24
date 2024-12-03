with open("Day3.in", "r") as f:
    data = f.readlines()
    data = data[0]

sum = 0
while True:
    try:
        index = data.find("mul(")
        index += 3
        print("found mul(")

    except Exception:
        break

    valid_phrase = False
    j = 1
    nums = ""
    while True:
        current_char = data[index + j]
        if current_char.isnumeric():
            nums += current_char
        elif current_char == ",":
            nums += " "
        elif current_char == ")" and " " in nums:
            valid_phrase = True
            break
        else:
            break

        j += 1
    
    if valid_phrase:
        print(nums)
        a, b = list(map(int, nums.split()))
        sum += a * b
        print("found one")
        if a == 89 and b == 379:
            break

    indexes_to_remove = []
    for j in range(3):
        indexes_to_remove.append(index + j)
    
    new_data = ""
    for i, char in enumerate(data):
        if i not in indexes_to_remove:
            new_data += char

    data = new_data    

print(sum)