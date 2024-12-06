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

# print(position)


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
        # for c in contents:
        #     print(c)
        # print("------------------------------")
        for i in range(1, limit):
            # depending on the direction, set the whole straight path as "X" until...
            x = position[0]+path[direction][0]*i
            y = position[1]+path[direction][1]*i

            # never hit obstacle "#"
            if x >= 0 and x <= maxRow and y >= 0 and y <= maxCol and contents[x][y] != "#":
                # print(x, y)
                contents[x] = contents[x][:y] + "X" + contents[x][y+1:]
                path_x.append([(x, y), direction])
                # current_position = (x-path[direction][0], y-path[direction][1])
                # position = (x, y)

            # hit obstacle "#"
            elif x >= 0 and x <= maxRow and y >= 0 and y <= maxCol and contents[x][y] == "#":
                hit.append((x, y))
                # rotate direction after hitting obstacle
                # print(direction)
                position = (x-path[direction][0], y-path[direction][1])
                # print(position)

                if direction == "^":
                    direction = ">"
                elif direction == ">":
                    direction = "v"
                elif direction == "v":
                    direction = "<"
                else:
                    direction = "^"
                # print(direction)
                break

            # or if go out-of-bound
            elif x < 0 or x > maxRow or y < 0 or y > maxCol:
                position = (x-path[direction][0], y-path[direction][1])
                oob = True

            if oob:
                break
    return path_x, hit


path_x, hit = trace_path(direction, position, contents)

# for c in contents:
#     print(c)

sum = 0

for c in contents:
    sum += c.count("X")
    # sum += c.count("^")

print(sum)

# PART 2

# the barrel must be placed on the current path marked with "X"
# if any of the one barrel result in going into a new path, then it won't work

# print(path_x)

# contents is the mapped out path
# original is the original empty map
# path_x is all the X mark

path_x.append([(original_position), "^"])
direction = "^"

total = 0
unknown = 0
dot = 0

replacement_x = [c[0] for c in path_x]
replacement_x = list(set(replacement_x))

for idx, c in enumerate(replacement_x):
    # print("Executing...")
    # print(c[0])
    print(idx)
    position = original_position
    direction = "^"
    new_path_x = []

    new_map = original.copy()
    new_map[c[0]] = new_map[c[0]][:c[1]] + "#" + new_map[c[0]][c[1]+1:]
    # for m in new_map:
    #     print(m)

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
            # print(x)
            # print(y)

            # never hit obstacle "#"
            if x >= 0 and x <= maxRow and y >= 0 and y <= maxCol and new_map[x][y] != "#":
                if contents[x][y] == "X" and [(x, y), direction] not in new_path_x:
                    new_path_x.append([(x, y), direction])
                    # print("Continue")
                elif [(x, y), direction] in new_path_x:
                    # print("SUCCEED")
                    # print(c[0])
                    # print("----------------------")
                    total += 1
                    oob = True
                elif contents[x][y] == ".":
                    # print((x, y))
                    # print(direction)
                    # print([(x, y), direction])
                    # print(new_path_x)
                    # print("Got into . path")
                    dot += 1
                    oob = True
                    flag = "fail"
                else:
                    print(idx)
                    unknown += 1
                    oob = True
                    flag = "fail"

            # hit obstacle "#"
            elif x >= 0 and x <= maxRow and y >= 0 and y <= maxCol and new_map[x][y] == "#":

                # print("HIT #")
                position = (x-path[direction][0], y-path[direction][1])
                # print(position)

                if direction == "^":
                    direction = ">"
                elif direction == ">":
                    direction = "v"
                elif direction == "v":
                    direction = "<"
                else:
                    direction = "^"
                # print(direction)
                break

            # or if go out-of-bound
            elif x < 0 or x > maxRow or y < 0 or y > maxCol:
                position = (x-path[direction][0], y-path[direction][1])
                # print("OOB")
                oob = True

            if oob:
                break

print(total)
print(unknown)
print(dot)
