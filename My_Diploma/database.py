import json
from person import Person


class Database:
    def __init__(self):
        self.people = []

    def add_person(self, person):
        self.people.append(person)

    def search(self, query):
        query = query.lower()
        return [
            person for person in self.people
            if query in person.first_name.lower()
            or query in person.family_name.lower()
            or query in person.patronymic.lower()
        ]

    def save_to_file(self, filename):
        with open(filename, "w", encoding="utf-8") as file:
            json.dump([person.__dict__ for person in self.people], file, indent=4, ensure_ascii=False, default=str)

    def load_from_file(self, filename):
        try:
            with open(filename, "r", encoding="utf-8") as file:
                data = json.load(file)
                self.people = []
                for item in data:
                    person = Person(
                        first_name=item["first_name"],
                        family_name=item["family_name"],
                        patronymic=item["patronymic"],
                        birth_date=item["birth_date"],
                        death_date=item["death_date"],
                        gender=item["gender"]
                    )
                    self.people.append(person)
            return True
        except FileNotFoundError:
            print("File not found!")
            return False
        except json.JSONDecodeError:
            print("Invalid file format!")
            return False
