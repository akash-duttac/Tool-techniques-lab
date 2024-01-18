#swap without 3rd variable
a = int(input("Enter a: "))
b = int(input("Enter b: "))
a = a + b
b = a - b
a = a - b
print(f"a = {a}, b = {b}")