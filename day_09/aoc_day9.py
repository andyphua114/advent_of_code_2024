with open('input.txt') as f:
    contents = f.readlines()
    content = contents[0]
    contents = [c for c in content]

# print(contents)

maxLength = len(contents)
maxId = maxLength//2
# print(maxId)

raw_sequence = []
total_odd = 0
total_even = 0

for idx, i in enumerate(contents):
    if idx % 2 == 0:  # check even, if so, then is block value
        block_value = idx//2
        sequence = str(block_value) * int(i)
        total_even += int(i)
    else:
        sequence = "." * int(i)
        total_odd += int(i)
    raw_sequence.append(sequence)

new_sequence = [r for r in "".join(raw_sequence) if r != "."]
reverse_sequence = [r for r in "".join(raw_sequence) if r != "."][::-1]

end = False
swap_index = -1

# print(new_sequence)
# print(reverse_sequence)

final_sequence = []

front_pointer = 0
rear_pointer = 0

total_diff = total_even - total_odd

total_run = 0

for idx, i in enumerate(contents):

    if idx % 2 == 0:  # check even, if so, then is block value
        block_value = idx//2
        sequence = new_sequence[front_pointer:front_pointer+int(i)]
        final_sequence.append(sequence)
        front_pointer += int(i)
    else:
        sequence = reverse_sequence[rear_pointer:rear_pointer+int(i)]
        final_sequence.append(sequence)
        rear_pointer += int(i)

    if front_pointer > total_diff:
        front_pointer += int(contents[idx+1])
        sequence = new_sequence[front_pointer:front_pointer +
                                int(contents[idx+1])]
        final_sequence.append(sequence)
        rear_pointer += int(contents[idx+1])
        sequence = reverse_sequence[rear_pointer:rear_pointer +
                                    int(contents[idx+1])]
        final_sequence.append(sequence)
        break


total_sequence = [i for sequence in final_sequence for i in sequence]
# print(total_sequence)
# space = new_sequence.count(".")
# tentative_space = space
# print(space)

# new_sequence_reversed = new_sequence[::-1]
# count_file = 0
# count_space = 0
# for i in new_sequence_reversed:
#     if i == ".":
#         count_space += 1
#         tentative_space -= 1
#     else:
#         count_file += 1
#     if count_file == tentative_space:
#         break

# new_space = space = tentative_space

# files_sequence = [(f, g)
#                   for (f, g) in enumerate(new_sequence) if g != "."][::-1]
# print(files_sequence)

# replacement_sequence = files_sequence[0:new_space]
# print(replacement_sequence)

# print(new_sequence)

# reverse_idx = -1

# for idx, i in enumerate(new_sequence):
#     if i == ".":
#         while new_sequence[reverse_idx] == ".":
#             reverse_idx -= 1
#         new_sequence[idx] = new_sequence[reverse_idx]
#         new_sequence[reverse_idx] = "."
#         reverse_idx -= 1
#     if len(new_sequence[idx+1:]) == new_sequence[idx+1:].count("."):
#         break

# print(new_sequence)

total = 0

for idx, i in enumerate(total_sequence):
    if i == ".":
        break
    else:
        total += idx * int(i)

print(total)
