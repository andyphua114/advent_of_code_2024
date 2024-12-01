with open('input.txt') as f:
    contents = f.readlines()

# PART 1

# split the left list and right list
left_list = [c.strip().split(" ")[0] for c in contents]
right_list = [c.strip().split(" ")[-1] for c in contents]

# sort both lists
left_list.sort()
right_list.sort()

# pair up the elements from left and right list based on index position using zip
matched_list = zip(left_list, right_list)

# calculate the diff between paired elements and sum up all the diffs
print(sum([abs(int(m[0])-int(m[1])) for m in matched_list]))

# PART 2

# since the similarity score will be zero if the element in left list does not appear in right list
# or vice versa, use set intersect to keep overlapped elements

overlapped = list(set(left_list).intersection(set(right_list)))

# count the number of times the overlapped elements appear in right list
# then add as running sum

sum = 0

for o in overlapped:
    sum += int(o) * right_list.count(o)

print(sum)
