#Project 2: Tip Calculator

print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? ₹"))
tip_percent = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
no_of_people = int(input("How many people to split the bill? "))
final_bill = ((tip_percent / 100) * total_bill + total_bill) / no_of_people
print(f"Each person should pay: {final_bill:.2f}")


# Day 2 Project: Tip Calculator
# Python Concepts Learned / Practiced:
# - print() function
# - input() function
# - Variables
# - Type casting (int(), float())
# - Arithmetic operators (+, /, *)
# - Order of operations
# - f-strings
# - Format specifier (:.2f)
