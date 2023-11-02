a = int(input("Please enter your first nubmer: "))
b = int(input("Please enter your second nubmer: "))
x = a * b
for i in range(max(a, b), a * b + 1):
    if i % a == 0 and i % b == 0:
        x = i
        break
print("the K-M-M is:", x)