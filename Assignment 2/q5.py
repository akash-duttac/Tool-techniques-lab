n = int(input("Enter the no. of items: "))
if n < 10:
    print(f"Cost = {12*n}")
elif n >= 10 and n < 100:
    print(f"Cost = {10*n}")
else:
    print(f"Cost = {7*n}")
