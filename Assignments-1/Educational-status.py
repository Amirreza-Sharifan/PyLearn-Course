print("Hello, in here you can know about your Educational Status")
a=float(input("Enter your Num-1: "))
b=float(input("Enter your Num-2: "))
c=float(input("Enter your Num-3: "))
average = (a+b+c)/3
if average >= 17:
    print("Your Average is:", average, ",Congratulations your status is Great")
elif 17 > average >= 12:
    print("Your Average is:", average, ",Not bad your status is Normal")
elif average < 12:
    print("Your Average is:", average, ",Sorry your status is Fail")