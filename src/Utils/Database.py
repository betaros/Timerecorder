import sqlite3
from sqlite3 import Error
import pathlib
from src.Utils.Utils import get_project_root
import datetime


database = pathlib.Path(get_project_root(), "timeRecorder.db")


def create_connection():
    conn = None
    try:
        conn = sqlite3.connect(database)
    except Error as e:
        print(e)

    return conn


def create_table(conn):
    sql_create_time_table = """ CREATE TABLE IF NOT EXISTS timetable (
                                                id integer PRIMARY KEY,
                                                begin_date timestamp,
                                                lunch_time integer, 
                                                end_date timestamp 
                                            ); """

    try:
        c = conn.cursor()
        c.execute(sql_create_time_table)
    except Error as e:
        print(e)


def insert_begin_date(conn, element):
    create_table(conn)

    sql_insert_element = f""" INSERT INTO timetable (begin_date) VALUES (?)"""
    element_tuple = (element,)

    try:
        c = conn.cursor()
        c.execute(sql_insert_element, element_tuple)
    except Error as e:
        print(e)


def add_begin_date(time: datetime):
    conn = create_connection()

    if conn is not None:
        insert_begin_date(conn, time)
    else:
        print("Unable to insert data into database.")

    conn.close()


def add_lunch_time(duration: int):
    conn = create_connection()

    if conn is not None:
        insert_begin_date(conn, duration)
    else:
        print("Unable to insert data into database.")

    conn.close()


def add_end_date(time: datetime):
    conn = create_connection()

    if conn is not None:
        insert_begin_date(conn, time)
    else:
        print("Unable to insert data into database.")

    conn.close()


add_begin_date(datetime.datetime.now())
add_begin_date(datetime.datetime.now())
add_begin_date(datetime.datetime.now())
