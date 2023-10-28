print("Welcome to the converting time from Seconde to Hour")
print("first you should enter your secondes time")
while 1==1:
    second = input("Enter the (Secondes): ")
    if second == "exit":
        break
    else:
        second = int(second) 
        if second >= 0:
            hours = second // 3600
            minutes = (second % 3600) // 60
            seconds = second % 60
            print("Your time is:",hours,":",minutes,":",seconds)
        else:
         print("Please enter non-negative values for hour, minute, and second.")