from sympy import symbols, Eq, solve
x = symbols('x')
a = float(input("Enter the a coefficient: "))
b = float(input("Enter the b coefficient: "))
c = float(input("Enter the c coefficient: "))
d = float(input("Enter the d coefficient: "))

equation = Eq(a*x**3 + b*x**2 + c*x + d, 0)
solutions = solve(equation, x)

print("The roots of the equation:")
for solution in solutions:
    print(solution)