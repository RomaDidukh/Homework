import json
import re
import os

def create_file():
    try:
        f = open("database/persons.json", "w")
        f.write("[]")
        f.close()
    except IOError as a:
        print("Error occurred while creating file:", a)

def get_all_humans() -> list:
    try:
        f = open("database/persons.json", "r")
    except FileNotFoundError:
        try:
            if os.path.exists("database"):
                create_file()
            else:
                os.mkdir("database")
                create_file()
            f = open("database/persons.json", "r")
        except IOError as b:
            print("Error occurred while creating or opening file:", b)
    try:
        data = json.loads(f.read())
    except ValueError as c:
        print("Error occurred while parsing JSON:", c)
        data = []
    finally:
        f.close()
    return data

def write_new_human(human: dict):
    data = get_all_humans()
    if len(data) < 1:
        human["id"] = 1
    else:
        human["id"] = len(data) + 1
    data.append(human)
    try:
        file = open("database/persons.json", "w")
        data = json.dumps(data)
        file.write(data)
        file.close()
    except IOError as f:
        print("Error occurred while writing to file:", f)

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
                print("This email already exists in the database")
                el["email"] = input("Enter new email: ")

            while not check_email(el["email"]):
                print("Email is not correct")
                el["email"] = input("Enter new email: ")

    try:
        file = open("database/persons.json", "w")
        data = json.dumps(data)
        file.write(data)
        file.close()
    except IOError as o:
        print("Error occurred while writing to file:", o)