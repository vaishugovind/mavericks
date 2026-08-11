#Movie Ticket Booking Summary
#reading user input
customer_name=input()
age=int(input())
Number_of_tickets=int(input())

#calculation
if age < 12:
    price=Number_of_tickets * 120
elif age >= 12 and age <=59:
    price=Number_of_tickets * 200
else:
    price=Number_of_tickets * 150

if Number_of_tickets >= 5:
    discount=0.10 * price
else:
    discount=0

final_amount=price-discount
print(f"Customer Name:{customer_name}")
print(f"Age:{age}")
print(f"Number of Tickets:{Number_of_tickets}")
print(f"Final Amount:Rs.{final_amount}")
    