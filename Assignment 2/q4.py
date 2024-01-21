no = int(input("Enter the no. of credits: "))
if no <= 23:
    print("Freshman")
elif no >= 24 and no <= 53:
    print("Sophomore")
elif no >= 54 and no <= 83:
    print("Junior")
else:
    print("Senior")