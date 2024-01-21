def are_close(num1, num2, tolerance=0.001):
    return abs(num1 - num2) <= tolerance

# Get user input for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Check if the numbers are close or not
if are_close(num1, num2):
    print("Close")
else:
    print("Not close")
