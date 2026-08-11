# Bus Seat Availability Manager
seats = [
    "Available",
    "Booked",
    "Available",
    "Available",
    "Booked",
    "Available",
    "Booked",
    "Available"
]

# Display all seats with their status
for i in range(len(seats)):
    print(f"Seat {i + 1}: {seats[i]}")

# Ask user to pick a seat
seat_number = int(input("\nEnter seat number to book: "))
index = seat_number - 1  # convert to 0-based index

if seats[index] == "Available":
    seats[index] = "Booked"
    print("Seat booked successfully.")
else:
    print("Seat is already booked.")

# Count totals
total_seats = len(seats)
booked_seats = seats.count("Booked")
available_seats = seats.count("Available")

print(f"\nTotal Seats: {total_seats}")
print(f"Booked Seats: {booked_seats}")
print(f"Available Seats: {available_seats}")