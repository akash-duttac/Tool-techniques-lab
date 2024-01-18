import math as m
print("Enter the sides of a triangle")
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
s = (a+b+c)/2
print(f"Area of triangle = {m.sqrt(s*(s-a)*(s-b)*(s-c))}")