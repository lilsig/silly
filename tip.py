#tip calculator

print("Welcome to the tip calculator")

total = float(input("What was the total bill? $"))
tip = (float(input("What percentage tip would you like to give? 10, 12, or 15? ")) / 100)
people = int(input("How many people to split the bill? "))

new_total = total + (total * tip)
split_cost = round(new_total / people, 2)

print(f"Each person should pay: ${split_cost}")
