def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n * factorial(n-1)

x = int(input("For e^x, Enter the value of x: "))
total = 0
for i in range(x):
    total += x**i/factorial(i)
print(f"e^{x} = {total}")