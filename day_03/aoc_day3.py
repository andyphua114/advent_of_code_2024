import re

# PART 1


def calc_sum(string):

    # pattern to match mul(num,num)
    pattern = re.compile(r"mul\((\d+,\d+)\)")

    match = re.findall(pattern, string)

    # convert the number to interger
    m = [[int(num) for num in m.split(",")] for m in match]

    # calculate the sum by multiply integers within each mul()
    sum = 0
    for num in m:
        sum += num[0] * num[1]

    return sum


with open('input.txt') as f:
    contents = f.readlines()

part1_sum = 0
for c in contents:
    part1_sum += calc_sum(c)

print(part1_sum)

# PART 2

part2_sum = 0

# the input should be treated as one long string
string = "".join(contents)

split_string = string.split("do()")

# after splitting by "do()",
# the splitted element will either be valid if it doesn't have don't()
# or split by "don't()" and anything to the left (which is before) of it will be valid
for substring in split_string:
    split_substring = substring.split("don't()")
    part2_sum += calc_sum(split_substring[0])

print(part2_sum)
