left_list = []
right_list = []

# open and read file to extract ids
# read line by line, first element in first list, second element in second list
# so, separate the lists according to their respective column (left vs. right)

with open('input.txt', 'r') as file:
    file = file.readlines()
    # input is a long string with spaces, so need to split it, to separate numbers
    for nums in range(len(file)):
        file[nums] = file[nums].split(' ')
    # now can extract first and last element, ignoring garbage in between, to get id numbers
    for id_num in file:
        left_list.append(int(id_num[0]))
        # slicing right id number since new line escape character at the end
        right_list.append(int(id_num[-1][:-1]))

# sort each list in ascending order
# use existing sort method

left_list.sort()
right_list.sort()

# compare each element of each list, one by one, finding the difference
# loop through indices, to harmonize search through both lists
# add difference to the sum of differences

sum_of_differences = 0

for num in range(len(left_list)):
    difference = abs(left_list[num] - right_list[num])
    sum_of_differences += difference

# return sum of differences
print(sum_of_differences)