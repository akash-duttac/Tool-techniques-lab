def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n * factorial(n-1)

n = int(input("Enter n: "))
total = 0
for i in range(1,n+1):
    total += 1/factorial(i)
print(f"Sum = {total}")