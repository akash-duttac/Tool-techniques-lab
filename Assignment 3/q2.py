import random
for i in range(10):
    a = random.randint(1,10)
    b = random.randint(1,10)
    ans = int(input(f"Question {i+1}: {a} x {b} = "))
    if ans == a*b:
        print("Right!")
    else:
        print("Wrong. The answer is", a*b)