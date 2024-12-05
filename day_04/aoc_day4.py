with open('input.txt') as f:
    contents = f.readlines()

contents = [c.strip() for c in contents]

maxCol = len(contents[0])-1
maxRow = len(contents)-1

# PART 1

# get all combinations of the coordinates in the grid
combinations = [(x, y) for x in range(maxRow+1) for y in range(maxRow+1)]


def return_letter(contents, x, y):

    # direction in up, down, left, right, topleft, topright, bottomleft, bottomright
    rowDirection = [-1, 1, 0, 0, -1, -1, 1, 1]
    colDirection = [0, 0, -1, 1, -1, 1, -1, 1]

    maxCol = len(contents[0])-1
    maxRow = len(contents)-1

    all_words = []
    # go through all eight directions, and form the 4-letter word whenever possible (not out-of-bound)
    for coord in zip(rowDirection, colDirection):
        # store the current letter
        word = contents[x][y]

        exit = False
        for i in range(1, 4):
            # check whether out-of-bound
            if i*coord[0]+x >= 0 and i*coord[0]+x <= maxRow and i*coord[1]+y >= 0 and i*coord[1]+y <= maxCol:
                word += contents[i*coord[0]+x][i*coord[1]+y]
            else:
                exit = True  # if out-of-bound, then exit loop
                break
            if exit:
                break
        all_words.append(word)

    return all_words


four_letters_list = []

for c in combinations:
    four_letters_list += return_letter(contents, c[0], c[1])

# check how many are valid "XMAS"
print(four_letters_list.count("XMAS"))

# PART 2

# get all combinations of the coordinates in the grid
combinations = [(x, y) for x in range(maxRow+1) for y in range(maxRow+1)]

# we are looking for a pattern where center is "A"
# topleft is "M", topright is "S", btmleft is "M", btmright is "S"
# if you unfold it, it will be AMSMS if you search from topleft to topright to btmleft to btmright


def return_cross_letter(contents, x, y):

    # direction in topleft, topright, bottomleft, bottomright
    crossRowDirection = [-1, -1, 1, 1]
    crossColDirection = [-1, 1, -1, 1]

    maxCol = len(contents[0])-1
    maxRow = len(contents)-1

    all_cross_words = []

    exit = False

    # store the current letter
    word = contents[x][y]

    # go through all four directions, and check the word whenever possible (not out-of-bound)
    for coord in zip(crossRowDirection, crossColDirection):

        if word[0] != "A":
            word = ""
            break

        # check whether out-of-bound
        if coord[0]+x >= 0 and coord[0]+x <= maxRow and coord[1]+y >= 0 and coord[1]+y <= maxCol:
            word += contents[coord[0]+x][coord[1]+y]
        else:
            break

    if len(word) > 0:
        all_cross_words.append(word)

    return all_cross_words


cross_letters_list = []

for c in combinations:
    cross_letters_list += return_cross_letter(contents, c[0], c[1])

# check how many are valid "X-MAS"
print(cross_letters_list.count("AMSMS")+cross_letters_list.count("ASSMM") +
      cross_letters_list.count("ASMSM")+cross_letters_list.count("AMMSS"))
