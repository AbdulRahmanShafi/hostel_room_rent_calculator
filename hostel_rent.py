## Inputs we need from the users
# Total rent amount
# Total food ordered
# Electricity bill
# Water bill
# Internet bill
# Total number of people sharing the rent

# Output
# Total amount per person to pay

rent = int(input("Enter the total rent amount = "))
food = int(input("Enter the total food ordered = "))
electricity = int(input("Enter the electricity bill = "))
water = int(input("Enter the water bill = "))
internet = int(input("Enter the amount of internet bill = "))
num_people = int(input("Enter the total number of people sharing the rent = "))

output = (rent + food + electricity + water + internet) / num_people
print("Total amount per person to pay = ", output)