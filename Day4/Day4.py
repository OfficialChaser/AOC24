with open("Day4.in", "r") as f:
    data = [i for i in f.readlines()]

word = "XMAS"

def is_xmas(txt):
    return txt == word or txt[::-1] == word

def horiz_test(line, i):
    if i + len(word) - 1 >= len(line):
        return False
    
    txt = ""
    for j in range(len(word)):
        txt += line[i + j]

    return is_xmas(txt)

def vertical_test(line_num, i):
    if line_num + len(word) - 1 >= len(data):
        return False

    txt = ""
    for j in range(len(word)):
        txt += data[line_num + j][i]
    
    return is_xmas(txt)

def forward_diagonal_test(line_num, i):
    if line_num + len(word) - 1 >= len(data):
        return False
    
    if i + len(word) - 1 >= len(data[0].strip('\n')):
        return False
    
    
    txt = ""
    for j in range(len(word)):
        txt += data[line_num + j][i + j]

    print(txt)
    return is_xmas(txt)

def backward_diagonal_test(line_num, i):
    if line_num + len(word) - 1 >= len(data):
        return False
    
    if i < len(word) - 1:
        return False
    
    txt = ""
    for j in range(len(word)):
        txt += data[line_num + j][i - j]

    return is_xmas(txt)

## PART 1 ##
'''sum = 0
for line_num, line in enumerate(data):
    for i, char in enumerate(line):
        if char == "X" or char == "S":
            sum += horiz_test(line, i)
            sum += vertical_test(line_num, i)
            sum += forward_diagonal_test(line_num, i)
            sum += backward_diagonal_test(line_num, i)


print(sum)'''

## PART 2 ##
word = "MAS"
sum2 = 0
for line_num, line in enumerate(data):
    for i, char in enumerate(line):
        if char == "M" or char == "S":
            sum2 += forward_diagonal_test(line_num, i) and backward_diagonal_test(line_num, i + 2)

print(sum2)