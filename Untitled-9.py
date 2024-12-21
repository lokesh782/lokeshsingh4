# Take user input for marks
marks = float(input("Enter your marks: "))

# Determine the grade based on the marks
if 90 <= marks <= 100:
    grade = "A"
elif 80 <= marks < 90:
    grade = "B"
elif 70 <= marks < 80:
    grade = "C"
else:
    grade = "Fail"

# Display the grade
print(f"Your grade is: {grade}")

