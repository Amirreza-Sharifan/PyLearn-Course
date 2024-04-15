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