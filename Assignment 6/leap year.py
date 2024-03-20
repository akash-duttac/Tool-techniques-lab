year = int(input("Enter year: "))
if year % 4==0:
    print(f"{year} is a leap year")
elif year %4==0 and year%100 ==0 and year%400==0:
    print("Leap year")
else:
    print(f"{year} not a leap year")