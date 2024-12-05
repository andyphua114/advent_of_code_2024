with open('test.txt') as f:
    contents = f.readlines()

contents = [c.strip() for c in contents]

maxCol = len(contents[0])-1
maxRow = len(contents)-1

print(maxCol)
print(maxRow)


def check_direction(contents, direction, current, rowIndex, colIndex):

    maxCol = len(contents[0])-1
    maxRow = len(contents)-1

    def check_next(current):
        if current == "X":
            return "M"
        elif current == "M":
            return "A"
        elif current == "A":
            return "S"
        else:
            return "End"

    if direction == "up":
        coord = (rowIndex-1, colIndex)
    elif direction == "down":
        coord = (rowIndex+1, colIndex)
    elif direction == "left":
        coord = (rowIndex, colIndex-1)
    elif direction == "right":
        coord = (rowIndex, colIndex+1)
    elif direction == "topleft":
        coord = (rowIndex-1, colIndex-1)
    elif direction == "topright":
        coord = (rowIndex-1, colIndex+1)
    elif direction == "btmleft":
        coord = (rowIndex+1, colIndex-1)
    elif direction == "btmright":
        coord = (rowIndex+1, colIndex+1)

    if coord[0] >= 0 and coord[0] <= maxRow and coord[1] >= 0 and coord[1] <= maxCol:
        if contents[coord[0]][coord[1]] != check_next(current):
            return coord
        else:
            return False


combinations = [(x, y) for x in range(maxRow+1) for y in range(maxRow+1)]

for coord in combinations:
    rowIndex = coord[0]
    colIndex = coord[1]

    current = contents[rowIndex][colIndex]

    if rowIndex == 0 and colIndex == 0:
        # check right, btmright, down
        coord = check_direction(contents, "right", current, rowIndex, colIndex)
        if coord:
            contents[coord[0]] = contents[coord[0]][:coord[1]] + "." + \
                contents[coord[0]][coord[1]+1:]

        coord = check_direction(contents, "btmright",
                                current, rowIndex, colIndex)
        if coord:
            contents[coord[0]] = contents[coord[0]][:coord[1]] + "." + \
                contents[coord[0]][coord[1]+1:]

        coord = check_direction(contents, "down", current, rowIndex, colIndex)
        if coord:
            contents[coord[0]] = contents[coord[0]][:coord[1]] + "." + \
                contents[coord[0]][coord[1]+1:]

    elif rowIndex == 0 and colIndex == maxCol:
        # check left, btmleft, down
        coord = check_direction(contents, "left", current, rowIndex, colIndex)
        if coord:
            contents[coord[0]] = contents[coord[0]][:coord[1]] + "." + \
                contents[coord[0]][coord[1]+1:]

        coord = check_direction(contents, "btmleft",
                                current, rowIndex, colIndex)
        if coord:
            contents[coord[0]] = contents[coord[0]][:coord[1]] + "." + \
                contents[coord[0]][coord[1]+1:]

        coord = check_direction(contents, "down", current, rowIndex, colIndex)
        if coord:
            contents[coord[0]] = contents[coord[0]][:coord[1]] + "." + \
                contents[coord[0]][coord[1]+1:]

for c in contents:
    print(c)
