#user input
name = input("Last name, First name: ")

#find comma in string
comma_index = name.index(',')

#extract first name from string, using comma position + 1 as slice delimiter, and strip any excess whitespace
first_name = name[comma_index + 1:].strip()

#output first name to user
print(first_name)