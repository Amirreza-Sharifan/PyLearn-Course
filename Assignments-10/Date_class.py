class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def add_days(self, days):
        #Add the number of days to the current date.
        ...

    def subtract_days(self, days):
        #Reduce the number of days from the current date
        ...

    def compare(self, other_date):
        #Compare this date with another date
        ...