from dataclasses import dataclass, field
from datetime import datetime, date, time
from typing import ClassVar

from app.services.util import generate_unique_id, date_lower_than_today_error, event_not_found_error, \
    reminder_not_found_error, slot_not_available_error


# TODO: Implement Reminder class here
@dataclass
class Reminder(EMAIL, SYSTEM):
    EMAIL:str= 'email'
    SYSTEM:str='system'
    date_time:datetime
    type:str = EMAIL
    def __init__(self,date_time, type = EMAIL):
        return date_time
    def __str__(self):
        return f"Reminder on {date_time} of type {type}"


# TODO: Implement Event class here
@dataclasses
class Event(id, title, description, date_, start_at, end_at):
    id:str
    title:str
    description:str
    date_:date
    start_at:time
    end_at:time


    def __init__(self, title, description, date_, start_at, end_at, id="..."):
        reminders:list[Reminder] = []
        id:str = generate_unique_id()

        def add_reminder(date_time:datetime, type_: str):
            Reminder.EMAIL = input("ingrese su email:")
            Reminder.date_time = input("ingrese la fecha en la que se realizara el evento:")
            title = input("ingrese el nombre del evento")
            description = input("ingrese la descripcion")
            start_at = input("ingrese la fecha y hora de inicio")
            end_at = input("ingrese la fecha y hora de finalizacion")
            reminders.append(id, Reminder.EMAIL, Reminder.date_time, title, description, start_at, end_at)

        def delete_reminder(reminder_index):
            reminder_index:int(input("ingrese el id del evento:"))
            if reminder_index in reminders:
                del reminders(reminder_index)
            else:
                return reminder_not_found_error()

        def __str__():
            return (f"ID: {id}"
                    f"Event title: {title}"
                    f"Description: {description}"
                    f"Time:{start_at} - {end_at}")


# TODO: Implement Day class here


# TODO: Implement Calendar class here
