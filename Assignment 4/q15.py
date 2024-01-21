# reverse an integer
n = int(input("Enter an integer: "))
reverse = 0
while n>0:
    temp = n%10
    reverse =  temp + reverse*10
    n //= 10
print("Reverse =", reverse)