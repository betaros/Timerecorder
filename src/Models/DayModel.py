import datetime


class DayModel:

    def __init__(self, begin: datetime, lunch: int, end: datetime):
        self.begin = begin
        self.lunch = lunch
        self.end = end
