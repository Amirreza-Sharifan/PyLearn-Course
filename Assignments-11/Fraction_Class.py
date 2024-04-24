import math

class Fraction:
    def __init__(self, numerator, denominator):
        #properties
        self.numerators = numerator
        self.denominators = denominator
        self.simplify()
        self.denominator_check()
    #methods
    def sum(self, fraction):
        numerator_sum = (self.numerators * fraction.denominators) + (fraction.numerators * self.denominators)
        denominator_sum = self.denominators * fraction.denominators
        result_sum = Fraction(numerator_sum, denominator_sum)
        return result_sum

    def subtract(self, fraction):
        numerator_sum = (self.numerators * fraction.denominators) - (fraction.numerators * self.denominators)
        denominator_sum = self.denominators * fraction.denominators
        result_sum = Fraction(numerator_sum, denominator_sum)
        return result_sum

    def multiply(self, fraction):
        numerator_multiply = self.numerators * fraction.numerators
        denominator_multiply = self.denominators * fraction.denominators
        result_multiply = Fraction(numerator_multiply, denominator_multiply)
        return result_multiply

    def divide(self, fraction):
        numerator_multiply = self.numerators * fraction.denominators
        denominator_multiply = self.denominators * fraction.numerators
        result_multiply = Fraction(numerator_multiply, denominator_multiply)
        return result_multiply

    def show(self):
        print(self.numerators,"/",self.denominators)


    def to_decimal(self):
        decimated = self.numerators / self.denominators
        print(decimated)
        return decimated
    
    def simplify(self):
        gcd = math.gcd(self.numerators, self.denominators)
        self.numerators //= gcd
        self.denominators //= gcd
        if self.denominators < 0:
            self.numerators *= -1
            self.denominators *= -1

    def denominator_check(self):
        if  self.denominators == 0:
            print("Your denominator is invalid, so other result will be showed like (1 / 0)")

print("Welcome to the Fraction program")
while True: 
    print("1: For -show- your Fraction press -1-") 
    print("2: For -sum- two Fraction press -2-")  
    print("3: For -subtract- two Fraction press -3-")
    print("4: For -multiply- two Fraction press -4-")
    print("5: For -divide- two Fraction press -5-")
    print("6: For -get decimal- a Fraction press -6-")
    print("0: For exit from program press -0-")    
    user_input = int(input("Pleas enter your request: "))
    if user_input == 1:
        numerator = int(input("Enter the -numerator section- of your number: "))
        denominator = int(input("Enter the -denominator section- of your number: "))
        num = Fraction(numerator , denominator)
        num.show()

    if user_input == 2:
        numerator_1 = int(input("Enter the -numerator section- of your First number: "))
        denominator_1 = int(input("Enter the -denominator section- of your First number: "))
        numerator_2 = int(input("Enter the -numerator section- of your Second number: "))
        denominator_2 = int(input("Enter the -denominator section- of your Second number: "))
        num_1 = Fraction(numerator_1 , denominator_1)
        num_2 = Fraction(numerator_2 , denominator_2)
        result = num_1.sum(num_2)
        result.show()

    if user_input == 3:
        numerator_1 = int(input("Enter the -numerator section- of your First number: "))
        denominator_1 = int(input("Enter the -denominator section- of your First number: "))
        numerator_2 = int(input("Enter the -numerator section- of your Second number: "))
        denominator_2 = int(input("Enter the -denominator section- of your Second number: "))
        num_1 = Fraction(numerator_1 , denominator_1)
        num_2 = Fraction(numerator_2 , denominator_2)
        result = num_1.subtract(num_2)
        result.show()

    if user_input == 4:
        numerator_1 = int(input("Enter the -numerator section- of your First number: "))
        denominator_1 = int(input("Enter the -denominator section- of your First number: "))
        numerator_2 = int(input("Enter the -numerator section- of your Second number: "))
        denominator_2 = int(input("Enter the -denominator section- of your Second number: "))
        num_1 = Fraction(numerator_1 , denominator_1)
        num_2 = Fraction(numerator_2 , denominator_2)
        result = num_1.multiply(num_2)
        result.show()

    if user_input == 5:
        numerator_1 = int(input("Enter the -numerator section- of your First number: "))
        denominator_1 = int(input("Enter the -denominator section- of your First number: "))
        numerator_2 = int(input("Enter the -numerator section- of your Second number: "))
        denominator_2 = int(input("Enter the -denominator section- of your Second number: "))
        num_1 = Fraction(numerator_1 , denominator_1)
        num_2 = Fraction(numerator_2 , denominator_2)
        result = num_1.divide(num_2)
        result.show()

    if user_input == 6:
        numerator = int(input("Enter the -numerator section- of your number: "))
        denominator = int(input("Enter the -denominator section- of your number: "))
        num = Fraction(numerator , denominator)
        num.to_decimal()

    if user_input == 0:
        break