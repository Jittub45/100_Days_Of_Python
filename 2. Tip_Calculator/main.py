
# If the bill was $150.00, split between 5 people, with 12% tip.
print("Welcome to tip calculator")
total_bill = float(input("Enter the bill amount: "))
# Each person should pay (150.00 / 5) * 1.12 = 33.6
tip_per = int(input("Enter tip percentage: "))
tip = total_bill * (tip_per / 100)
final_bill = total_bill + tip
# Format the result to 2 decimal places = 33.60
num_Of_Member = int(input("Enter number of member: "))
ind_bill = round(final_bill / num_Of_Member, 2)
# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
print(f"Individual bill of every person is {ind_bill}")
# Write your code below this line
