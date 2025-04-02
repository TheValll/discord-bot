import json
import os

PATH = os.path.join(os.path.dirname(__file__), "../bdd.json")
with open(PATH, "r") as file:
    data = json.load(file)
    birthdays = data["members"]

def get_birthday(date):
    result = []
    for member in birthdays:
        if member["member_birthday_date"] == date:
            result.append(member)
        else:
            continue

    return result