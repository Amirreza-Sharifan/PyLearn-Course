class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def sum(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def subtract(self, other):
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    def multiply(self, other):
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.imag * other.real + self.real * other.imag
        return ComplexNumber(real_part, imag_part)

    def show(self):
        if self.imag >= 0:
            print(self.real,"+",self.imag,"i")
            return f"{self.real} + {self.imag}i"
        else:
            print(self.real,"-",self.imag,"i")
            return f"{self.real} - {-self.imag}i"