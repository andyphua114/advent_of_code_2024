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
start_idx = 1
end_idx = len(contents)

file = []
for idx, c in enumerate(contents):
    if idx % 2 == 0:  # check even, if so, then is block value
        file.append((idx//2, c, start_position))
    start_position += c

space_digits = [int(i) for idx, i in enumerate(contents) if idx % 2 != 0]

space_info = []

idx = 1
for s, f in zip(space_digits, file[:-1]):
    space_info.append([idx, s, f[1]+f[2]])
    idx += 2

reverse_file = file[::-1]
new_file = []

space_idx_to_remove = end_idx

for index, f in enumerate(reverse_file[:-1]):

    for idx, space in enumerate(space_info):
        if f[1] < space[1]:
            new_file.append((f[0], f[1], space[2]))
            space_info[idx] = [space[0], space[1]-f[1], space[2]+f[1]]
            break
        elif f[1] == space[1]:
            new_file.append((f[0], f[1], space[2]))
            space_info = [s for s in space_info if s != space]
            break

    # we start checking from the file at the back
    # once we check that file, the space before is no longer valid for the files in front to fill
    # so we need to remove it
    space_idx_to_remove -= 2
    space_info = [s for s in space_info if s[0] != space_idx_to_remove]


new_file_number = [i[0] for i in new_file]
remaining = [i for i in file if i[0] not in new_file_number]

full = new_file + remaining

total = 0
for f in full:
    for i in range(f[1]):
        total += f[0] * (i + f[2])

print(total)
