# Expense Tracker
expenses = [250, 1200, 450, 800, 150, 2000, 350]

total_expense = sum(expenses)
average_expense = total_expense / len(expenses)
highest_expense = max(expenses)
lowest_expense = min(expenses)

above_500 = 0
below_or_equal_500 = 0

for amount in expenses:
    if amount > 500:
        above_500 += 1
    else:
        below_or_equal_500 += 1

print(f"Total Expense: {total_expense}")
print(f"Average Expense: {average_expense:.2f}")
print(f"Highest Expense: {highest_expense}")
print(f"Lowest Expense: {lowest_expense}")
print(f"Number of Expenses Above ₹500: {above_500}")
print(f"Number of Expenses Below or Equal to ₹500: {below_or_equal_500}")

print("\nExpenses Above Average:\n")
for amount in expenses:
    if amount > average_expense:
        print(amount)