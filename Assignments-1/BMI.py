print("Welcome, here we are going to find the status of your body health")
print("Please cheack and input the right number in SI dimention")
a=float(input("Please Enter your weight(kg): "))
b=float(input("Please Enter your height(m): "))
BMI=a/(b**2)
if BMI <= 18.5:
    print("Your BMI is:", BMI,", Your Status is - Under Weight -")
elif 18.5 < BMI <= 24.9:
    print("Your BMI is:", BMI,", Your Status is - Normal Weight -")
elif 25 < BMI <= 29.9:
    print("Your BMI is:", BMI,", Your Status is - Over Weight -")
elif 30 < BMI <= 34.9:
    print("Your BMI is:", BMI,", Your Status is - Obestiy -")
elif 35 < BMI <= 39.9:
    print("Your BMI is:", BMI,", Your Status is - Extreme Obestiy -")
elif BMI >= 40:
    print("Your BMI is:", BMI,", Your Status is - Too Weight -")