# Take user input for salary and credit score
salary = float(input("Enter your salary: "))
credit_score = int(input("Enter your credit score: "))

# Check eligibility based on salary and credit score
if salary >= 50000 and credit_score >= 700:
    print("Eligible")
else:
    print("Not Eligible")
