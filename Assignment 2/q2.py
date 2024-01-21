t = float(input("Enter a temperature: "))
choice = int(input("Enter 1 (for Celsius) or 2 (for Fahrenheit): "))
if choice == 1:
    print(f"{t} C = {t*9/5 + 32} F")
else:
    print(f"{t} F = {5/9*(t-32)} C")