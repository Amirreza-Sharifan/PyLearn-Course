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

print("Welcome to the Complex Number program")
while True: 
    print("1: For -showing- your complex number press -1-") 
    print("2: For -sum- 2 complex number press -2-")  
    print("3: For -subtract- 2 complex number press -3-")
    print("4: For -multiply- 2 complex number press -4-")
    print("0: For exit from program press -0-")    
    user_input = int(input("Pleas enter your request: "))
    if user_input == 1:
        real = int(input("Enter the Real section of your number: "))
        image = int(input("Enter the Image section of your number: "))
        num = ComplexNumber(real , image)
        num.show()

    if user_input == 2:
        real_1 = int(input("Enter the Real section of your first number: "))
        image_1 = int(input("Enter the Image section of your first number: "))
        real_2 = int(input("Enter the Real section of your second number: "))
        image_2 = int(input("Enter the Image section of your second number: "))
        num_1 = ComplexNumber(real_1 , image_1)
        num_2 = ComplexNumber(real_2 , image_2)
        result = num_1.sum(num_2)
        result.show()

    if user_input == 3:
        real_1 = int(input("Enter the Real section of your first number: "))
        image_1 = int(input("Enter the Image section of your first number: "))
        real_2 = int(input("Enter the Real section of your second number: "))
        image_2 = int(input("Enter the Image section of your second number: "))
        num_1 = ComplexNumber(real_1 , image_1)
        num_2 = ComplexNumber(real_2 , image_2)
        result = num_1.subtract(num_2)
        result.show()

    if user_input == 4:
        real_1 = int(input("Enter the Real section of your first number: "))
        image_1 = int(input("Enter the Image section of your first number: "))
        real_2 = int(input("Enter the Real section of your second number: "))
        image_2 = int(input("Enter the Image section of your second number: "))
        num_1 = ComplexNumber(real_1 , image_1)
        num_2 = ComplexNumber(real_2 , image_2)
        result = num_1.multiply(num_2)
        result.show()

    if user_input == 0:
        break