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