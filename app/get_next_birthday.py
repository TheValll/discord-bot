import os
import json

from datetime import datetime, timedelta

PATH = os.path.join(os.path.dirname(__file__), "../bdd.json")
with open(PATH, "r") as file:
    data = json.load(file)
    birthdays = data["members"]


def get_next_birthday(date, server_id):
    result = {}
    current_date = datetime.strptime(date, "%d/%m")

    while True:
        date_str = current_date.strftime("%d/%m")
        for member in birthdays:
            if member["member_birthday_date"] == date_str and member["server_id"] == server_id:
                result = member
                return result
        current_date += timedelta(days=1)