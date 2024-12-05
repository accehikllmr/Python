# analyze data to determine how many reports are indeed safe
# to be safe, must be increasing or decreasing and increases or decreases do not exceed 3

# open file and extract numbers into lists, splitting to separate numbers
with open('input.txt', 'r') as file:
    file = file.readlines()
    print(file)
    for line in range(len(file)):
        file[line] = file[line].split(' ')
    # removing next line character from last number in each sequence
    for line in file:
        line[-1] = line[-1][:]
    # converting all numbers in lists into integers
    for line in file:
        for num in range(len(line)):
            line[num] = int(line[num])

safe_reports = file
print(file)

# rather than eliminating all that are not in order, simply check through single iteration
# iterate through each element in list
# iterate through each element in sublist
# save current number, if next is smaller OR more than three bigger then break and delete element

#problem calculation for gaps, since some gaps missing, perhaps specifically on ends

for report in safe_reports:
    # store all gaps as a set, since duplicates do not matter
    gaps = set()
    # variable to update previous number
    n = 0
    for number in report[1:]:
        # setting first number in list as previous number, since its value alone is not sufficient to evaluate report
        previous_num = report[n]
        # calculating gaps and adding to list
        gap = number - previous_num
        gaps.add(gap)
        n += 1

    # convert to list in order to sort
    gaps_list = sorted(gaps)

    # remove reports whose gaps contain opposite signs
    if gaps_list[0] < 0 < gaps_list[-1]:
        safe_reports.remove(report)

    #
    check_set = {1, 2, 3}

    for gap in gaps:
        if (abs(gap) not in check_set) and (report in safe_reports):
            safe_reports.remove(report)


    '''
    # iterate through set to find values larger than three
    gaps_sum = 0
    for gap in gaps:
        # remove all reports which have a gap larger than 3
        if gap == 0 or abs(gap) > 3:
            safe_reports.remove(report)
            print(str(report), str(gaps), '0 or bigger than 3')
            break
        # otherwise, calculate sum of gaps, if larger than sum of the set then there are mixed signs
        gaps_sum += abs(gap)
    if report in safe_reports and abs(sum(gaps)) != gaps_sum:
        safe_reports.remove(report)
        print(str(report), str(gaps), 'plus minus')
        continue

    if report in safe_reports:
        print(str(report), str(gaps), "accepted")
    

for i in safe_reports:
    print(i)

    '''
print(len(safe_reports))