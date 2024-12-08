from itertools import combinations

with open('input.txt') as f:
    contents = [c.strip() for c in f.readlines()]

maxRow = len(contents)
maxCol = len(contents[0])

unique_antenna = {}
# find unique antennas
# then pair them up

for idxRow, c in enumerate(contents):
    for idxCol, x in enumerate(c):
        if x != "." and x not in unique_antenna.keys():
            unique_antenna[x] = [(idxRow, idxCol)]
        elif x != ".":
            unique_antenna[x].append((idxRow, idxCol))


def check_valid(coord, value, maxRow, maxCol):
    x, y = coord
    if coord not in value and x >= 0 and x <= maxRow-1 and y >= 0 and y <= maxCol-1:
        return coord
    else:
        return False


antinode = []

for key, value in unique_antenna.items():
    antenna_combi = list(combinations(value, 2))
    for antenna in antenna_combi:
        first, second = antenna
        if sum(first) < sum(second):
            diff = (second[0]-first[0], second[1]-first[1])
        else:
            diff = (first[0]-second[0], first[1]-second[1])
        for i in range(2):
            coord_minus = (antenna[i][0]-diff[0], antenna[i][1]-diff[1])
            coord_plus = (antenna[i][0]+diff[0], antenna[i][1]+diff[1])
            an_minus = check_valid(coord_minus, value, maxRow, maxCol)
            an_plus = check_valid(coord_plus, value, maxRow, maxCol)
            if an_minus:
                antinode.append(an_minus)

            if an_plus:
                antinode.append(an_plus)

print(len(set(antinode)))

# PART 2

antinode = []

for key, value in unique_antenna.items():
    antenna_combi = list(combinations(value, 2))
    for antenna in antenna_combi:
        first, second = antenna
        antinode.append(first)
        antinode.append(second)
        if sum(first) < sum(second):
            diff = (second[0]-first[0], second[1]-first[1])
        else:
            diff = (first[0]-second[0], first[1]-second[1])

        # step in forward direction
        for i in range(2):
            for j in range(1, maxRow):
                coord_minus = (antenna[i][0]-j*diff[0],
                               antenna[i][1]-j*diff[1])
                coord_plus = (antenna[i][0]+j*diff[0], antenna[i][1]+j*diff[1])
                if coord_minus[0] < 0 or coord_minus[0] > maxRow-1 or coord_minus[1] < 0 or coord_minus[1] > maxCol-1:
                    pass
                else:
                    antinode.append(coord_minus)

                if coord_plus[0] < 0 or coord_plus[0] > maxRow-1 or coord_plus[1] < 0 or coord_plus[1] > maxCol-1:
                    break
                else:
                    antinode.append(coord_plus)

      # step in backward direction
        for i in range(2):
            for j in range(-1, -maxRow, -1):
                coord_minus = (antenna[i][0]-j*diff[0],
                               antenna[i][1]-j*diff[1])
                coord_plus = (antenna[i][0]+j*diff[0], antenna[i][1]+j*diff[1])
                if coord_minus[0] < 0 or coord_minus[0] > maxRow-1 or coord_minus[1] < 0 or coord_minus[1] > maxCol-1:
                    pass
                else:
                    antinode.append(coord_minus)

                if coord_plus[0] < 0 or coord_plus[0] > maxRow-1 or coord_plus[1] < 0 or coord_plus[1] > maxCol-1:
                    break
                else:
                    antinode.append(coord_plus)

print(len(set(antinode)))
