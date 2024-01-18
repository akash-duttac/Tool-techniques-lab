print("Enter three no.s")
a = int(input())
b = int(input())
c = int(input())
temp = a
a = b
b = c
c = temp
print(f"After swapping\na = {a}, b = {b}, c = {c}")