class Time:
    def __init__(self, hour, minute, second):
        self.hours = hour
        self.minutes = minute
        self.seconds = second
        self.fix_time()
    def sum_time(self,time):
        second_new = self.seconds + time.seconds
        minute_new = self.minutes + time.minutes
        hour_new = self.hours + time.hours
        result_sum = Time(hour_new, minute_new, second_new)
        return result_sum
    def subtract_time(self, time):
        second_new = self.seconds - time.seconds
        minute_new = self.minutes - time.minutes
        hour_new = self.hours - time.hours
        result_subtract = Time(hour_new, minute_new, second_new)
        return result_subtract
    
    def second_to_time(self, second):
        hours = second // 3600
        remainder_minutes = second % 3600
        minutes = remainder_minutes // 60
        seconds = remainder_minutes % 60
        result = Time(hours, minutes, seconds)
        print("your",second,"seconds, is:")
        result.show_time()
        return result

    def time_to_second(self):
        final_second = (self.hours * 3600) + (self.minutes * 60) + (self.seconds)
        print("Your time has",final_second,"seconds.")
        return final_second

    def show_time(self):
        print(self.hours,":",self.minutes,":",self.seconds)

    def fix_time(self):
        if self.seconds >= 60:
            self.seconds -= 60
            self.minutes += 1

        if self.minutes >= 60:
            self.minutes -= 60
            self.hours += 1

        if self.seconds < 0 :
            self.seconds += 60
            self.minutes -= 1

        if self.minutes < 0:
            self.minutes += 60
            self.hours -= 1

        if self.hours < 0:
            self.hours = 0

    def to_tehran_time(self):
        self.minutes += 30
        self.hours += 3
        print("The Tehran time is:")
        self.show_time()

print("Welcome to the Time program")
while True: 
    print("1: For -showing- your time press -1-") 
    print("2: For -sum- two time press -2-")  
    print("3: For -subtract- two time press -3-")
    print("4: For -get second to time- press -4-")
    print("5: For -get time to second- press -5-")
    print("6: For -change GMT to tehran time- press -6-")
    print("0: For exit from program press -0-")    
    user_input = int(input("Pleas enter your request: "))
    if user_input == 1:
        hour = int(input("Enter the -hour section- of your time: "))
        minute = int(input("Enter the -minute section- of your time: "))
        second = int(input("Enter the -second section- of your time: "))
        result = Time(hour , minute, second)
        result.show_time()

    if user_input == 2:
        hour_1 = int(input("Enter the -hour section- of your first time: "))
        minute_1 = int(input("Enter the -minute section- of your first time: "))
        second_1 = int(input("Enter the -second section- of your first time: "))
        hour_2 = int(input("Enter the -hour section- of your second time: "))
        minute_2 = int(input("Enter the -minute section- of your second time: "))
        second_2 = int(input("Enter the -second section- of your second time: "))
        time_1 = Time(hour_1 , minute_1, second_1)
        time_2 = Time(hour_2 , minute_2, second_2)
        result = time_1.sum_time(time_2)
        result.show_time()

    if user_input == 3:
        hour_1 = int(input("Enter the -hour section- of your first time: "))
        minute_1 = int(input("Enter the -minute section- of your first time: "))
        second_1 = int(input("Enter the -second section- of your first time: "))
        hour_2 = int(input("Enter the -hour section- of your second time: "))
        minute_2 = int(input("Enter the -minute section- of your second time: "))
        second_2 = int(input("Enter the -second section- of your second time: "))
        time_1 = Time(hour_1 , minute_1, second_1)
        time_2 = Time(hour_2 , minute_2, second_2)
        result = time_1.subtract_time(time_2)
        result.show_time()

    if user_input == 4:
        second = int(input("Enter your seconds to change in a time: "))
        result.second_to_time(second)
    
    if user_input == 5:
        hour = int(input("Enter the -hour section- of your time: "))
        minute = int(input("Enter the -minute section- of your time: "))
        second = int(input("Enter the -second section- of your time: "))
        result = Time(hour , minute, second)
        result.time_to_second()
        
    if user_input == 6:
        hour = int(input("Enter the -hour section- of your time: "))
        minute = int(input("Enter the -minute section- of your time: "))
        second = int(input("Enter the -second section- of your time: "))
        result = Time(hour , minute, second)
        result.to_tehran_time()

    if user_input == 0:
        break