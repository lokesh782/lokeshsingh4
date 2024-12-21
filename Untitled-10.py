# Input: Ask for the weight of the package
weight = float(input("Enter the weight of the package (in kg): "))

# Input: Ask if the delivery is urgent
urgent = input("Is the delivery urgent? (yes/no): ").strip().lower()

# Initialize the delivery cost
cost = 0

# Determine the base cost based on the weight of the package
if weight < 5:
    cost = 5
elif 5 <= weight <= 20:
    cost = 10
else:
    cost = 20

# Check if the delivery is urgent and add extra cost if necessary
if urgent == 'yes':
    cost += 5

# Output the final delivery cost
print(f"The total delivery cost is: ${cost}")
