#taking user inputs for body specifications
weight = float(input("What is your weight in kilograms? "))
height = float(input("What is your height in centimeters? "))

#converting height from centimeters to meters
height = height / 100

#calculating body mass index using above user inputs
body_mass_index = round(weight / (height ** 2), 2)

#output result of calculation to user
print(body_mass_index)