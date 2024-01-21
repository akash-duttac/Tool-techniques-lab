#compute sum of digits of the integer
n = int(input("Enter an integer: "))
total = 0
while n>0:
    temp = n%10
    total += temp
    n //= 10
print("Total =", total)