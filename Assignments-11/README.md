# PyLearn Course - Assignment 11

This repository contains the assignments and projects for Session 11 of the PyLearn course. In this repository, you can find different tasks and examples specifically designed to enhance your understanding of Python programming and its applications.

## ComplexNumber Class

The `ComplexNumber` class is designed to handle basic arithmetic operations for complex numbers in Python. Each instance of this class represents a complex number with a real part and an imaginary part.

### Methods

- `__init__(self, real, imag)`: Initializes a new instance of the ComplexNumber class.
- `sum(self, other)`: Adds two complex numbers.
- `subtract(self, other)`: Subtracts one complex number from another.
- `multiply(self, other)`: Multiplies two complex numbers.
- `show(self)`: Prints and returns the complex number in a readable format.

### Example Usage

Here's how you can use the `ComplexNumber` class to perform operations with complex numbers:

```python
# Create two complex numbers
num1 = ComplexNumber(3, 2)
num2 = ComplexNumber(1, 7)

# Add the two numbers
result_sum = num1.sum(num2)
result_sum.show()  # Output: 4 + 9i

# Subtract the second number from the first
result_subtract = num1.subtract(num2)
result_subtract.show()  # Output: 2 - 5i

# Multiply the two numbers
result_multiply = num1.multiply(num2)
result_multiply.show()  # Output: -11 + 23i
```
## Fraction Class

The `Fraction` class is designed to perform arithmetic operations and manage fractions in Python. It includes methods for addition, subtraction, multiplication, division, simplification, and conversion to decimal.

### Methods

- `__init__(self, numerator, denominator)`: Initializes a new Fraction instance. Simplifies the fraction and checks for a valid denominator.
- `sum(self, fraction)`: Adds two fractions.
- `subtract(self, fraction)`: Subtracts one fraction from another.
- `multiply(self, fraction)`: Multiplies two fractions.
- `divide(self, fraction)`: Divides one fraction by another.
- `show(self)`: Prints the fraction in the form of `numerator/denominator`.
- `to_decimal(self)`: Converts the fraction to a decimal.
- `simplify(self)`: Simplifies the fraction using the greatest common divisor.
- `denominator_check(self)`: Checks if the denominator is zero and prints a warning if so.

### Example Usage

Here's how you can use the `Fraction` class to perform operations with fractions:

```python
# Create two fractions
frac1 = Fraction(1, 2)
frac2 = Fraction(3, 4)

# Add the two fractions
result_sum = frac1.sum(frac2)
result_sum.show()  # Output: 5/4

# Subtract the second fraction from the first
result_subtract = frac1.subtract(frac2)
result_subtract.show()  # Output: -1/4

# Multiply the two fractions
result_multiply = frac1.multiply(frac2)
result_multiply.show()  # Output: 3/8

# Divide the first fraction by the second
result_divide = frac1.divide(frac2)
result_divide.show()  # Output: 2/3

# Convert the result of the division to decimal
result_divide.to_decimal()  # Output: 0.6666666666666666
```
## Carpet Generator

The `Carpet Generator` is a simple Python script that creates a visual representation of a carpet using emojis. The carpet pattern is generated based on user input for the size of the carpet, which must be an odd number.

### Functionality

- The script prompts the user to enter an odd number to determine the size of the carpet.
- If the entered number is even, the script will inform the user that the number must be odd.
- The carpet is visually represented using two emojis: "🟦" for the border and "⬜️" for the interior.
- The pattern is a square with a border of "🟦" surrounding the "⬜️" interior, forming a frame.

### Example Usage

Here's how you can interact with the `Carpet Generator`:

1. Run the script.
2. When prompted, input an odd number, for example, 5. You can also exit the script by entering 0.
3. The script will generate and display the carpet pattern.

```python
Welcome to the Carpet Generator, please input a number for generating your carpet
Your n must be an odd number, please enter your (n), or press (0) for exiting: 5
🟦🟦🟦🟦🟦
🟦⬜️⬜️⬜️🟦
🟦⬜️⬜️⬜️🟦
🟦⬜️⬜️⬜️🟦
🟦🟦🟦🟦🟦
```
## Time Class

The `Time` class is designed to manage and manipulate time values in Python. It supports operations such as addition, subtraction, conversion between seconds and time, and normalization of time values.

### Methods

- `__init__(self, hour, minute, second)`: Initializes a new Time instance with hours, minutes, and seconds. Automatically adjusts the time if values are out of range.
- `sum_time(self, time)`: Adds two Time instances.
- `subtract_time(self, time)`: Subtracts one Time instance from another.
- `second_to_time(self, second)`: Converts a given number of seconds to a Time instance.
- `time_to_second(self)`: Converts the Time instance to seconds.
- `show_time(self)`: Prints the time in HH:MM:SS format.
- `fix_time(self)`: Normalizes the time so that minutes and seconds are within their correct ranges.
- `to_tehran_time(self)`: Adjusts the time to Tehran time, adding 3 hours and 30 minutes.

### Example Usage

Here's how you can interact with the `Time` class to perform time operations:

```python
# Create two time instances
time1 = Time(2, 45, 30)
time2 = Time(3, 50, 45)

# Add the two times
result_sum = time1.sum_time(time2)
result_sum.show_time()  # Output: 6:36:15 (Assuming no initial overflow)

# Subtract the second time from the first
result_subtract = time1.subtract_time(time2)
result_subtract.show_time()  # Output: -1:5:15 (Corrected by fix_time to be negative or zero where appropriate)

# Convert 5000 seconds to Time
result_from_seconds = time1.second_to_time(5000)
result_from_seconds.show_time()  # Output: 1:23:20

# Convert Time to seconds
seconds = time1.time_to_second()
# Output will print "Your time has 9990 seconds."

# Adjust time to Tehran Time
time1.to_tehran_time()
time1.show_time()  # Output: 6:15:30