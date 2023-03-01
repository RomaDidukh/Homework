import json
import re

class Base:
    file = ""

    def __init__(self):
        pass

    def generate_dict(self):
        raise NotImplementedError

    def save(self):
        self.get_all()
        with open(self.file, "r") as f:
            data = json.load(f)
        with open(self.file, "w") as f:
            obj_dict = self.generate_dict()
            obj_dict["id"] = len(data) + 1 if len(data) > 1 else 1
            data.append(obj_dict)
            json.dump(data, f)

    @classmethod
    def get_all(cls):
        with open(cls.file, "r") as f:
            data = json.load(f)
        for obj in data:
            print(obj)


class Plant(Base):
    file = "database/plants.json"

    def __init__(self, name, address):
        super().__init__()
        self.name = name
        self.address = address

    def generate_dict(self):
        return {
            "name": self.name,
            "address": self.address
        }


class Employee(Base):
    file = "database/employees.json"

    def __init__(self, name, email, plant_id):
        super().__init__()
        self.name = name
        self.email = email
        self.plant_id = plant_id

    def generate_dict(self):
        return {
            "name": self.name,
            "email": self.email,
            "plant_id": self.plant_id
        }


def is_valid_email(email):
    match = re.search(r'[\w.-]+@[\w.-]+', email)
    if match:
        return True
    else:
        return False
