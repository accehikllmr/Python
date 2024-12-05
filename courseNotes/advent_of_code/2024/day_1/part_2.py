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

# instead of finding sum, now looking at list to calculate a similarity score
# similarity score is for each number in the left list, how many time it shows up in the right list, times itself
# iterate through each item in the left list, even duplicates
# even simpler than iterating, would be to find count in each list and multiply by number in question
# for this, we can create a set to remove duplicates, for faster iteration
left_set = set(left_list)
similarity_score = 0

# iterate through each element in set (condensed left list, to avoid duplicate iterations)
for num in left_set:
    # count number of appearances in each list
    left_count = left_list.count(num)
    right_count = right_list.count(num)
    # calculate score using derived formula
    similarity_score += num * left_count * right_count

print(similarity_score)