with open('input.txt') as f:
    contents = f.readlines()

contents = [c.strip() for c in contents]

original = contents.copy()

maxCol = len(contents[0])-1
maxRow = len(contents)-1

# PART 1

# get all combinations of the coordinates in the grid
combinations = [(x, y) for x in range(maxRow+1) for y in range(maxRow+1)]

direction = "^"

for c in combinations:
    if contents[c[0]][c[1]] == direction:
        original_position = c
        position = c
        break


def trace_path(direction, position, contents):

    oob = False
    hit = []
    path_x = []

    maxCol = len(contents[0])-1
    maxRow = len(contents)-1

    # set boundary of grid
    if maxRow > maxCol:
        limit = maxRow
    else:
        limit = maxCol

    # up, down, left, right
    path = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}

    while not oob:
        for i in range(1, limit):
            # depending on the direction, set the whole straight path as "X" until...
            x = position[0]+path[direction][0]*i
            y = position[1]+path[direction][1]*i

            # never hit obstacle "#"
            if x >= 0 and x <= maxRow and y >= 0 and y <= maxCol and contents[x][y] != "#":
                contents[x] = contents[x][:y] + "X" + contents[x][y+1:]
                path_x.append([(x, y), direction])

            # hit obstacle "#"
            elif x >= 0 and x <= maxRow and y >= 0 and y <= maxCol and contents[x][y] == "#":
                hit.append((x, y))
                # rotate direction after hitting obstacle
                position = (x-path[direction][0], y-path[direction][1])

                if direction == "^":
                    direction = ">"
                elif direction == ">":
                    direction = "v"
                elif direction == "v":
                    direction = "<"
                else:
                    direction = "^"
                break

            # or if go out-of-bound
            elif x < 0 or x > maxRow or y < 0 or y > maxCol:
                position = (x-path[direction][0], y-path[direction][1])
                oob = True

            if oob:
                break
    return path_x, hit


path_x, hit = trace_path(direction, position, contents)

sum = 0

for c in contents:
    sum += c.count("X")

print(sum)

# PART 2

# the obstacle must be placed on the current path marked with "X"

# contents is the mapped out path
# original is the original empty map
# path_x is all the X mark

path_x.append([(original_position), "^"])
direction = "^"

total = 0

replacement_x = [c[0] for c in path_x]

# get unique list of coordinates to replace "X" with "#"
replacement_x = list(set(replacement_x))

for idx, c in enumerate(replacement_x):

    print(idx)
    position = original_position
    direction = "^"
    new_path_x = []

    new_map = original.copy()
    # put an obstacle
    new_map[c[0]] = new_map[c[0]][:c[1]] + "#" + new_map[c[0]][c[1]+1:]

    maxCol = len(contents[0])-1
    maxRow = len(contents)-1

    # set boundary of grid
    if maxRow > maxCol:
        limit = maxRow
    else:
        limit = maxCol

    # up, down, left, right
    path = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}

    oob = False

    while not oob:
        for i in range(1, limit+1):

            # depending on the direction, set the whole straight path as "X" until...
            x = position[0]+path[direction][0]*i
            y = position[1]+path[direction][1]*i

            # never hit obstacle "#"
            if x >= 0 and x <= maxRow and y >= 0 and y <= maxCol and new_map[x][y] != "#":
                if [(x, y), direction] not in new_path_x:
                    new_path_x.append([(x, y), direction])
                # if the same coord + direction happens again, means it is going to go on same loop
                elif [(x, y), direction] in new_path_x:
                    total += 1
                    oob = True
                else:
                    oob = True
                    flag = "fail"

            # hit obstacle "#"
            elif x >= 0 and x <= maxRow and y >= 0 and y <= maxCol and new_map[x][y] == "#":

                position = (x-path[direction][0], y-path[direction][1])

                if direction == "^":
                    direction = ">"
                elif direction == ">":
                    direction = "v"
                elif direction == "v":
                    direction = "<"
                else:
                    direction = "^"
                break

            # or if go out-of-bound
            elif x < 0 or x > maxRow or y < 0 or y > maxCol:
                position = (x-path[direction][0], y-path[direction][1])
                oob = True

            if oob:
                break

print("Part 1: {}".format(sum))
print("Part 2: {}".format(total))
