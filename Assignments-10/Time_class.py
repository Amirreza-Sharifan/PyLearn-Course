class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def set_time(self, hour, minute, second):
        #resetting the time
        ...

    def add_time(self, hours=0, minutes=0, seconds=0):
        #Add time to existing time
        ...

    def subtract_time(self, hours=0, minutes=0, seconds=0):
        #Decrease time from available time
        ...

    def time_to_seconds(self):
        #Convert time to seconds
        ...

    def seconds_to_time(self, seconds):
        #Convert seconds to time (hours, minutes, seconds)
        ...

    def format_24hr(self):
        #Time display in 24-hour format
        ...

    def format_12hr(self):
        #Time display in 12-hour format
        ...