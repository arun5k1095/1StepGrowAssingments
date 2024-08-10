principal = float(input("Enter the principal amount: "))
rate_of_interest = float(input("Enter the rate of interest (in %): "))
time = float(input("Enter the time (in years): "))

simple_interest = (principal * rate_of_interest * time) / 100

print(f"The simple interest is: {simple_interest:.2f}")
