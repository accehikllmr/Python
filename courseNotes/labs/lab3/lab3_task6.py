#user input
name = input("Last name, First name: ")

#find comma in string
comma_index = name.index(',')

#extract last name from string, using comma position as slice delimiter, and strip any excess whitespace
last_name = name[:comma_index].strip()

#output last name to user
print(last_name)