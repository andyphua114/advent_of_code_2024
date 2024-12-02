with open('input.txt') as f:
    contents = f.readlines()

report_str = [c.strip().split(" ") for c in contents]

# convert the levels into int from str
report_int = [[int(level) for level in r] for r in report_str]


# PART 1

# check if all increasing/decreasing; use sort and compare to original
# also use set to check if there are duplicated elements within list
report_increasing = []
report_decreasing = []
bad_report = []

for r in report_int:
    r_sorted = sorted(r, reverse=False)
    if r_sorted == r and len(set(r)) == len(r):
        report_increasing.append(r)
    elif sorted(r, reverse=True) == r and len(set(r)) == len(r):
        report_decreasing.append(r)
    else:
        bad_report.append(r)

valid_report = []

# diff between adjacent must be at most three
# no need check for at least one as adjacent duplicated elements are already not in list
for r in report_increasing:
    omit = False
    for pair in list(zip(r, r[1:])):
        if pair[1] - pair[0] > 3:
            omit = True   # once the diff between adj elements are more than 3, set omit so you don't append the report
            continue
    if not omit:
        valid_report.append(r)
    else:
        bad_report.append(r)

for r in report_decreasing:
    omit = False
    for pair in list(zip(r, r[1:])):
        if pair[0] - pair[1] > 3:
            omit = True
            continue
    if not omit:
        valid_report.append(r)
    else:
        bad_report.append(r)

print(len(valid_report))

# PART 2

# for this part, it can tolerate one bad level
# we check for those in bad_report

bad_report_sublists = []

# iteratively omit one element/"level" per report
for r in bad_report:
    sublists = [r[:i] + r[i+1:] for i in range(len(r))]
    bad_report_sublists.append(sublists)

tolerated_report = 0

# loop through the sub-reports
for subreport in bad_report_sublists:
    report_increasing = []
    report_decreasing = []
    bad_report = []

    for r in subreport:
        r_sorted = sorted(r, reverse=False)
        if r_sorted == r and len(set(r)) == len(r):
            report_increasing.append(r)
        elif sorted(r, reverse=True) == r and len(set(r)) == len(r):
            report_decreasing.append(r)
        else:
            bad_report.append(r)

    # diff between adjacent must be at most three
    # no need check for at least one as adjacent duplicated elements are already not in list
    for r in report_increasing:
        omit = False
        for pair in list(zip(r, r[1:])):
            if pair[1] - pair[0] > 3:
                omit = True   # once the diff between adj elements are more than 3, set omit so you don't append the report
                continue
        if not omit:
            tolerated_report += 1
            break   # as long as one sub-report meet the requirement, means it is a tolerated report

    for r in report_decreasing:
        omit = False
        for pair in list(zip(r, r[1:])):
            if pair[0] - pair[1] > 3:
                omit = True
                continue
        if not omit:
            tolerated_report += 1
            break

print(tolerated_report + len(valid_report))
