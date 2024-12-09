with open('input.txt') as f:
    contents = f.readlines()
    content = contents[0]
    contents = [int(c) for c in content]

maxLength = len(contents)
maxId = maxLength//2

file_idx = 0
space_idx = 0

# PART 1

# get the file block digits only, which are the even placed digit

fileblock_digits = [int(i) for idx, i in enumerate(contents) if idx % 2 == 0]
reverse_fileblock_digits = fileblock_digits[::-1]
space_digits = [int(i) for idx, i in enumerate(contents) if idx % 2 != 0]

reverse_value = [i for i in range(maxId, -1, -1)]

final = []

reverse_idx = 0

# there are no zero digit in the even position
for idx, i in enumerate(contents):
    if idx//2 >= reverse_value[reverse_idx]:
        final.append(
            (reverse_value[reverse_idx], reverse_fileblock_digits[reverse_idx]))
        break
    elif idx % 2 == 0:  # check even, if so, then is block value
        final.append((idx//2, i))
    else:
        # i is the number of space
        while i >= reverse_fileblock_digits[reverse_idx]:
            i = i - reverse_fileblock_digits[reverse_idx]
            final.append(
                (reverse_value[reverse_idx], reverse_fileblock_digits[reverse_idx]))
            reverse_fileblock_digits[reverse_idx] = 0
            reverse_idx += 1
        if i < reverse_fileblock_digits[reverse_idx] and i != 0:
            final.append((reverse_value[reverse_idx], i))
            reverse_fileblock_digits[reverse_idx] -= i

    # print(reverse_fileblock_digits)

# print(final)

total = 0
indice = 0
cnt = 0

for a, b in final:
    cnt = cnt + b
    while indice < cnt:
        total += a * indice
        indice += 1

print(total)

# PART 2

with open('input.txt') as f:
    contents = f.readlines()
    content = contents[0]
    contents = [int(c) for c in content]

start_position = 0

file = []

for idx, c in enumerate(contents):
    if idx % 2 == 0:  # check even, if so, then is block value
        file.append((idx//2, c, start_position))
    start_position += c

reversed_file = file[::-1]
# print(file)

space_digits = [int(i) for idx, i in enumerate(contents) if idx % 2 != 0]

# print(space_digits)
space_info = []

for s, f in zip(space_digits, file[:-2]):
    space_info.append([s, f[1]+f[2]])

# print(space_info)

new_file = []

for idx, f in enumerate(reversed_file[:-1]):
    restart = False
    for index, space in enumerate(space_info):
        if f[1] <= space[0]:
            # print(f[1])
            # print(index, space)
            # print(file[index][1])
            # print(file[index][2])
            new_f = (f[0], f[1], space_info[index][1])
            # print(new_f)
            # print("_______________________________________")
            new_file.append(new_f)
            reversed_file = [r for r in reversed_file if r != f]
            space_info[index][0] = space_info[index][0] - f[1]
            space_info[index][1] = space_info[index][1] + f[1]
            restart = True
            break
        if restart:
            break


# print(file)

new_file_number = [i[0] for i in new_file]
remaining = [i for i in file if i[0] not in new_file_number]

full = new_file + remaining

total = 0
for f in full:
    for i in range(f[1]):
        total += f[0] * (i + f[2])

print(total)
