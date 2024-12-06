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
                path_x.append([position, direction])
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

for x in path_x[18:19]:
    coord_x, coord_y = x[0]
    new_map = contents.copy()
    new_map[coord_x] = new_map[coord_x][:coord_y] + \
        "#" + new_map[coord_x][coord_y+1:]

    new_path_x = []

    oob = False

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
            x = original_position[0]+path[direction][0]*i
            y = original_position[1]+path[direction][1]*i

            # never hit obstacle "#"
            if x >= 0 and x <= maxRow and y >= 0 and y <= maxCol and contents[x][y] != "#":
                if contents[x][y] != "X" or (contents[x][y] == "X" and [(original_position), direction] not in path_x):
                    flag = "fail"
                    oob = True
                    break
                elif [(x, y), direction] not in new_path_x:
                    new_path_x.append([(original_position), direction])
                else:
                    flag = "succeed"
                    oob = True
                    break

            # hit obstacle "#"
            elif x >= 0 and x <= maxRow and y >= 0 and y <= maxCol and contents[x][y] == "#":

                original_position = (
                    x-path[direction][0], y-path[direction][1])

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
                original_position = (
                    x-path[direction][0], y-path[direction][1])
                flag = "fail"
                oob = True

            if oob:
                break

    if flag == "succeed":
        total += 1

print(total)
