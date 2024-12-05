with open('input.txt') as f:
    contents = f.readlines()

if "\n" in contents:
    split_index = contents.index("\n")
    # Split the list into two parts
    rules = contents[:split_index]
    updates = contents[split_index + 1:]

rules = [r.strip().split("|") for r in rules]
updates = [u.strip().split(",") for u in updates]

# PART 1

# create a dict to store based on X|Y, that Y must come after X
# X is the key, and Y is the value in a list

rule_check_after_dict = {}

for r in rules:
    if r[0] not in rule_check_after_dict.keys():
        rule_check_after_dict[r[0]] = [r[1]]
    else:
        if r[1] not in rule_check_after_dict[r[0]]:
            rule_check_after_dict[r[0]].append(r[1])

# create a dict to store based on X|Y, that X must come before Y
# Y is the key, and X is the value in a list
# e.g. 61,13,29
# but there may be no rule with 13|<number>. Hence in rule_check_after_dict, you won't have key 13
# so when you trying to check for number after 13 whether satisfies rule_check_after_dict, you get key error

rule_check_before_dict = {}

for r in rules:
    r = r[::-1]
    if r[0] not in rule_check_before_dict.keys():
        rule_check_before_dict[r[0]] = [r[1]]
    else:
        if r[1] not in rule_check_before_dict[r[0]]:
            rule_check_before_dict[r[0]].append(r[1])

correct = []
incorrects = []

for update in updates:

    valid = True

    for idx, u in enumerate(update):
        # need to check both direction, after and before
        # e.g. this case 61,13,29
        # for rule_check_afer_dict, you will first break because 13 not in dict
        # so you also need to check for 29 using rule_check_before dict to make sure condition is statisfied
        # in 61,13,29 case it will not because there is a rule 29|13

        # rule_check_after_dict for all elements after reference element
        for x in update[idx+1:]:
            if u not in rule_check_after_dict.keys():
                break
            elif x not in rule_check_after_dict[u]:
                valid = False
                break

        # rule_check_before_dict for all elements before reference element
        for x in update[0:idx]:
            if u not in rule_check_before_dict.keys():
                break
            elif x not in rule_check_before_dict[u]:
                valid = False
                break
    if valid:
        correct.append(update)
    else:
        incorrects.append(update)

sum = 0

for c in correct:
    middle_idx = len(c)//2
    middle_value = c[middle_idx]
    sum += int(middle_value)

print(sum)

# PART 2

# get all the updates that are incorrect
not_correct = incorrects.copy()

fixed_length = len(not_correct)
fixed = []

# keep looping until all are fixed
while len(fixed) != fixed_length:

    # for each incorrect update, we iterating fix it by swapping between reference element and it's adjacent
    for incorrect in not_correct:
        valid_before = True
        valid_after = True
        for idx, u in enumerate(incorrect):
            # rule_check_after_dict for all elements after reference element
            for x in incorrect[idx+1:]:
                if u not in rule_check_after_dict.keys():
                    break
                elif x not in rule_check_after_dict[u]:
                    temp = x
                    current_idx = incorrect.index(x)
                    incorrect[current_idx] = incorrect[idx]
                    incorrect[idx] = temp
                    valid_after = False
                    break

            # rule_check_before_dict for all elements before reference element
            for x in incorrect[0:idx]:
                if u not in rule_check_before_dict.keys():
                    break
                elif x not in rule_check_before_dict[u]:
                    temp = x
                    current_idx = incorrect.index(x)
                    incorrect[current_idx] = incorrect[idx]
                    incorrect[idx] = temp
                    valid_before = False
                    break

        if valid_before and valid_after:
            fixed.append(incorrect)
            not_correct.remove(incorrect)

sum = 0

for c in fixed:
    middle_idx = len(c)//2
    middle_value = c[middle_idx]
    sum += int(middle_value)

print(sum)
