# Enter the hours worked
hours = input("Enter the hours worked: ")

# Convert the hours string to a float
hours = float(hours)

# Enter the hourly pay rate
rate = input("Enter the hourly rate: ")

# Convert the rate string to a float
rate = float(rate)

# Multiply the hours and rate
resultPay = hours * rate

# Print the result
print(f"The gross pay is: {resultPay}")