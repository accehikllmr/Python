# get input
phone_number = input("Please give me your phone number: ")

# you can add any line of code between this line and the line with return
# calculating the number of digits that appear in the phone number
length = (phone_number.count('1') + phone_number.count('2') + phone_number.count('3')
          + phone_number.count('4') + phone_number.count('5') + phone_number.count('6')
          + phone_number.count('7') + phone_number.count('8') + phone_number.count('9')
          + phone_number.count('0'))

# determining if the number of digits in the phone number is of the desired length
correct_length = length == 10

#removing all valid characters from the phone number, to see whether any invalid characters are left over
invalid_characters = phone_number.replace('0', '').replace('1', '').replace('2','')\
    .replace('3', '').replace('4','').replace('5','').replace('6','')\
    .replace('7','').replace('8','').replace('9','').replace('-','')\
    .replace('(','').replace(')','').replace(' ','')

#after removing all of the valid characters, if the length of the string is not zero, then there are invalid characters in the string
no_invalid_characters = len(invalid_characters) == 0

#valid if the length is correct, with respect to digits, and there are no invalid characters
validity = correct_length and no_invalid_characters

# show result
print(validity)