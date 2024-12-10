with open('test.txt') as f:
    contents = f.readlines()

contents = [c.strip() for c in contents]

maxCol = len(contents[0])-1
maxRow = len(contents)-1

# find all value and coordinates

coord = []

for row_idx, content in enumerate(contents):
    for col_idx, c in enumerate(content):
        coord.append((int(c), row_idx, col_idx))

# find all the trailheads which is value 0

trailhead = [i for i in coord if i[0] == 0]

print(trailhead)

goal = []


def move(t, goal):
    value = t[0]
    x = t[1]
    y = t[2]

    step = {'up': (-1, 0),
            'down': (1, 0),
            'left': (0, -1),
            'right': (0, 1)}

    for direction, shift in step.items():
        new_x = x + shift[0]
        new_y = y + shift[1]
        if new_x >= 0 and new_x <= maxRow and new_y >= 0 and new_y <= maxCol and int(contents[new_x][new_y]) == value+1:
            print("Moving in: {}".format(direction))
            print("Shifting by: {}".format(shift))

            if value == 8 and int(contents[new_x][new_y]) == 9:
                goal.append((new_x, new_y))
                print("SUCCEED")
                print("---------------------------")
                return 1
            else:
                value = int(contents[new_x][new_y])
                x = new_x
                y = new_y
                print((value, x, y))
                print("---------------------------")
                move((value, x, y), goal)

    return 0


test = move(trailhead[0], goal)
print(goal)

# for t in trailhead:
#     value = t[0]
#     x = t[1]
#     y = t[2]

#     move = {'up': (-1, 0),
#             'down': (1, 0),
#             'left': (0, -1),
#             'right': (0, 1)}

#     for direction, shift in move.items():

#         new_x = x + shift[0]
#         new_y = y + shift[1]

#         if new_x > 0 and new_x <= maxRow and new_y > 0 and new_y <= maxCol:
#             next_value = contents[new_x][new_y]
#             if next_value == value + 1:
