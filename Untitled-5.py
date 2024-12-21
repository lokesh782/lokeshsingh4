# Input: Take two numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Compare the two numbers
if num1 > num2:
    print(f"The greater number is {num1}")
elif num2 > num1:
    print(f"The greater number is {num2}")
else:
    # If the numbers are equal, check if the number is positive, negative, or zero
    print("Both numbers are equal.")
    if num1 > 0:
        print("The number is positive.")
    elif num1 < 0:
        print("The number is negative.")
    else:
        print("The number is zero.")
