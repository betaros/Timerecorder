from src.Utils import Database
from src.Models import DayModel


def add_element(day_element: DayModel):
    Database.add_begin_date(day_element.get_start())
    Database.add_lunch_time(day_element.get_lunch())
    Database.add_end_date(day_element.get_end())


def edit_element(id, day_element: DayModel):
    Database.edit_begin_date(id, day_element.get_start())
    Database.edit_lunch_time(id, day_element.get_lunch())
    Database.edit_end_date(id, day_element.get_end())


def delete_element(id):
    Database.delete_element(id)


def show_element(id):
    Database.get_element(id)
