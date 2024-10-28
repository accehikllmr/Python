def is_valid_phone_number(number : str, position : int = 0, prior_validity : bool = True) -> bool:

    #indexing the current position of the character whose validity is being checked
    a = number[position]

    #identifiying the maximum index possible for the string, in order to prevent recursion from going out of range
    max_position = len(number) - 1

    #assessing whether the phone number is valid, using assessment from previous and current characters
    still_valid = prior_validity and (a.isdigit() or a.isspace() or a == '(' or a == ')' or a == '-')

    #variable for stopping recursion
    stop = position == max_position or not still_valid

    is_valid_phone_number(number, position + 1, still_valid)

    return still_valid

'''
# get input
phone_number = input("Please give me your phone number: ")

# calculating the number of digits that appear in the phone number
length = (phone_number.count('1') + phone_number.count('2') + phone_number.count('3')
          + phone_number.count('4') + phone_number.count('5') + phone_number.count('6')
          + phone_number.count('7') + phone_number.count('8') + phone_number.count('9')
          + phone_number.count('0'))

# determining if the number of digits in the phone number is of the desired length
correct_length = length == 10

# show result
print(correct_length) # You can modify this line as needed
'''

print(is_valid_phone_number("905-802-1758"))

#replace all valid characters by empty string, and if length is not zero, then string is invalid