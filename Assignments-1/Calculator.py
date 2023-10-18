import math

print("Welcome, This is my calculator that you can use for your solutions")
print("First: You can perform some mathematical operations here, including:")
print("+ : sum")
print("- : sub")
print("* : multiple")
print("/ : divide")
print("sin")
print("cos")
print("tan")
print("cot")
print("log")
print("Sqrt")
print("factorial")

operations = input("So, now choose your operation from above: ")

if operations=="+" or operations=="-" or operations=="*" or operations=="/":
    a = float(input("Enter Num-1: "))
    b = float(input("Enter Num-2: "))
else:
    c = float(input("Enter a Num: "))

if operations == "+":
    result = a + b
elif operations == "-":
    result = a - b
elif operations == "*":
    result = a * b
elif operations == "/":
    if b == 0:
        result = print("Error! try again")
    else:
        result = a / b
elif operations == "sin":
    radians = math.radians(c)
    result = math.sin(radians)
elif operations == "cos":
    radians = math.radians(c)
    result = math.cos(radians)
elif operations == "tan":
    radians = math.radians(c)
    result = math.tan(radians)
elif operations == "cot":
    radians = math.radians(c)
    result = 1 / math.tan(radians)
elif operations == "log":
    result = math.log(c)
elif operations == "Sqrt" or operations == "sqrt":
    result = math.sqrt(c)
elif operations == "factorial" or operations == "Factorialsqrt":
    result = math.factorial(int(c))

print("Result:", result)