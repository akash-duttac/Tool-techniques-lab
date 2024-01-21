n = int(input("Enter an integer: "))
count = 0
while n>0:
    count += 1
    n = n//10
print(f"No. in digits is {count}")