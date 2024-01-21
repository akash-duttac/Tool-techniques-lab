#cm to inch
cm = float(input("Enter length(in cm): "))
if cm < 0:
    print(f"Negative length!!")
else:
    print(f"{cm} cm = {2.54*cm} inches")