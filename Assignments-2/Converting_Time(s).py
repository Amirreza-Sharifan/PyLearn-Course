print("Welcome to the converting time from Hour to Seconde")
print("first you should enter your (seconde - minute - hour) sequently")
while 1==1:
    hour = input("Enter the (hour): ")
    if hour == "exit":
        break
    minute = input("Enter the (minute): ")
    second = input("Enter the (Second): ")
    if second == "exit":
        break
    else:
        second = int(second) 
        minute = int(minute) 
        hour = int(hour)
        if second >= 0 and minute >= 0 and hour >= 0:
            print("your time is:",hour,":",minute,":",second)
            total_seconds = (int(hour) * 3600) + (int(minute) * 60) + int(second)
            print("Your time in seconds is:", total_seconds)
        else:
         print("Please enter non-negative values for hour, minute, and second.")