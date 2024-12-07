from itertools import product
import math

with open('input.txt') as f:
    contents = f.readlines()

contents = [[int(x) for x in c.replace(":", "").strip().split(" ")]
            for c in contents]

# PART 1


def iterative_addmul(c):
    total = 0
    target = c[0]
    values = c[1:]

    length = len(c[1:])

    operations = ("add", "mul")

    combinations = list(product(operations, repeat=length-1))

    for operators in combinations:
        if operators[0] == "add":
            total = values[0] + values[1]
        else:
            total = values[0] * values[1]

        for op, c in zip(operators[1:], values[2:]):
            if op == "add":
                total += c
            else:
                total *= c

        if total == target:
            return target
    return 0


def first_check(c):
    target = c[0]
    values = c[1:]

    if math.prod(values) == target:
        return target
    elif sum(values) == target:
        return target
    else:
        return 0


total = 0

for c in contents:
    # need to check for 1 not in c[1:], else the rule of math.prod(c[1:]) < c[0] does not work
    # e.g. 455616000: 74 1 4 4 565 8 4 21
    if 1 not in c[1:] and math.prod(c[1:]) < c[0]:
        # print("All multiply falls short")
        continue

    if sum(c[:1]) > c[0]:
        # print("All addition exceeds")
        continue

    return_target = first_check(c)
    if return_target > 0:
        # print("SUCCEED")
        total += return_target
        continue

    return_target = iterative_addmul(c)
    if return_target > 0:
        # print("SUCCEED")
        total += return_target
        continue

print("Part 1: {}".format(total))

# PART 2


def iterative_addmul(c):
    total = 0
    target = c[0]
    values = c[1:]

    length = len(c[1:])

    operations = ("add", "mul", "concat")

    combinations = list(product(operations, repeat=length-1))

    for operators in combinations:
        if operators[0] == "add":
            total = values[0] + values[1]
        elif operators[0] == "mul":
            total = values[0] * values[1]
        else:
            total = int(str(values[0]) + str(values[1]))

        for op, c in zip(operators[1:], values[2:]):
            if op == "add":
                total += c
            elif op == "mul":
                total *= c
            else:
                total = int(str(total) + str(c))

        if total == target:
            return target
    return 0


def first_check(c):
    target = c[0]
    values = c[1:]

    if math.prod(values) == target:
        return target
    elif sum(values) == target:
        return target
    else:
        return 0


total = 0

for c in contents:

    # using all multiply or all sum as first round of check won't work here
    # due to concat can make a number much bigger than itself
    # use brute force way to check

    return_target = first_check(c)
    if return_target > 0:
        # print("SUCCEED")
        total += return_target
        continue

    return_target = iterative_addmul(c)
    if return_target > 0:
        # print("SUCCEED")
        total += return_target
        continue

print("Part 2: {}".format(total))
