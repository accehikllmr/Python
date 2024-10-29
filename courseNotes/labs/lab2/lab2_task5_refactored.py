#taking user inputs for body specifications, converting height immediately upon receiving input
weight = float(input("What is your weight in kilograms? "))
height = float(input("What is your height in centimeters? ")) / 100

#calculating body mass index using above user inputs
body_mass_index = round(weight / (height ** 2), 2)

#output result of calculation to user, added sentence to explain output
print(f"For a height of {height} meters and a weight of {weight} kilograms, the BMI is {body_mass_index}.")