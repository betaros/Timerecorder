import datetime


class DayModel:

    def __init__(self):
        self.start = None
        self.lunch = None
        self.end = None

    def set_start(self, start: datetime):
        self.start = start

    def get_start(self) -> datetime:
        return self.start

    def set_lunch(self, lunch: datetime):
        self.lunch = lunch

    def get_lunch(self) -> datetime:
        return self.lunch

    def set_end(self, end: datetime):
        self.end = end

    def get_end(self) -> datetime:
        return self.end
