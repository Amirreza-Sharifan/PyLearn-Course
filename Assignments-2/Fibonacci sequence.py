print("Welcome to the Fibonacci sequence")
print("In this program, you can display the Fibonacci sequence for as many numbers as you want.")
n = int(input("How many numbers of the sequence would you like to display? n = "))
a, b = 1, 1
print("Fibonacci Sequence (first " + str(n) + " elements):")
for i in range(n):
    print(a, end=", ")
    a, b = b, a + b