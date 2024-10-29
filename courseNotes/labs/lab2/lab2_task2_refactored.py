# specify the quantity of each type of vehicles
num_bicycles = int(input("How many bicycles? "))
num_tricycles = int(input("How many tricycles? "))
num_cars = int(input("How many cars? "))
num_trucks = int(input("How many trucks? "))
    
# calculate the number of wheels of each type of vehicles
total_bicycle_wheels = num_bicycles * 2
total_tricycle_wheels = num_tricycles * 3
total_car_wheels = num_cars * 4
total_truck_wheels = num_trucks * 18
    
# calculate the total number of wheels
total_wheels = total_bicycle_wheels + total_tricycle_wheels + total_car_wheels + total_truck_wheels

#output to screen, added sentence to explain final output
print(f"{num_bicycles} bicycles, {num_tricycles} tricycles, {num_cars} cars and {num_trucks} trucks have a total of {total_wheels} wheels.")