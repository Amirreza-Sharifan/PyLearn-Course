a = int(input("Please enter your first nubmer: "))
b = int(input("Please enter your second nubmer: "))
x = 1
for i in range(1, min(a, b) + 1):
    if a * b % i == 0:
        x = i
print("the B-M-M is:", x)