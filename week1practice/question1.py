# Write a python program that calculates the parking charge based on the number of hours a vehicle was parked

# Reading the user input
parking_hours = int(input())

# Calculating the parking charge
if parking_hours <= 2:
    charge = parking_hours * 30
elif parking_hours <= 5:
    charge = parking_hours * 25
else:
    charge = parking_hours * 20

# Adding service charge
if charge >= 150:
    service_charge = 0
else:
    service_charge = 20

final_amount = charge + service_charge
print(f"Final amount: Rs. {final_amount}")