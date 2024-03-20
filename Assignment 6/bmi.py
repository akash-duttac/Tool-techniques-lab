import numpy
h = [5.8, 6.2, 5.2, 4.5]
w = [65.3, 61.2, 35.6, 21.4]
bmi = []
for i in range(len(h)):
    bmi.append(w[i]/h[i]**2)
print(bmi)