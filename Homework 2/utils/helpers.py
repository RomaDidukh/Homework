import json
import re

def get_all_humans() -> list:
    f = open("database/persons.json", "r")
    data = json.loads(f.read())
    f.close()
    return data


def write_new_human(human: dict):
    data = get_all_humans()
    if len(data) < 1:
        human["id"] = 1
    else:
        human["id"] = len(data) + 1
    data.append(human)
    file = open("database/persons.json", "w")
    data = json.dumps(data)
    file.write(data)
    file.close()

def check_email(email):
    match = re.search(r'[\w.-]+@[\w.-]+', email)
    if match:
        return True
    else:
        return False

def is_email_unique(email):
    data = get_all_humans()
    for el in data:
        if el["email"] == email:
            return False
    return True

def edit_human(id):
    data = get_all_humans()
    for el in data:
        if el["id"] == id:
            el["first_name"] = input("Enter new first name: ")
            el["last_name"] = input("Enter new last name: ")
            el["email"] = input("Enter new email: ")

            while not is_email_unique(el["email"]):
                print("Еhis email already exists in the database")
                el["email"] = input("Enter new email: ")

            while not check_email(el["email"]):
                print("Email is not correct")
                el["email"] = input("Enter new email: ")

    file = open("database/persons.json", "w")
    data = json.dumps(data)
    file.write(data)
    file.close()

