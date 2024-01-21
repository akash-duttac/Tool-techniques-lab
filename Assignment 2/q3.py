temp = float(input("Enter the temperature in Celsius: "))
if temp < -273.15:
    print("The temperature is below absolute zero")
elif temp == -273.15:
    print("The temperature is absolute zero")
elif temp > -273.15 and temp < 0:
    print("The temperature is below freezing point")
elif temp >= 0 and temp < 100:
    print("The temperature is in normal range")
elif temp==100:
    print("The temperature is at boiling point")
else:
    print("The temperature is above the boiling point")