import json
from datetime import datetime


class Person:
    def __init__(self, first_name, family_name="", patronymic="", birth_date=None, death_date=None, gender=""):
        if not first_name:
            raise ValueError("First name is required.")
        if not birth_date:
            raise ValueError("Birth date is required.")
        if gender not in ["m", "f", ""]:
            raise ValueError("Gender must be 'm', 'f', or empty.")

        self.first_name = first_name.strip().capitalize()
        self.family_name = family_name.strip().capitalize() if family_name else ""
        self.patronymic = patronymic.strip().capitalize() if patronymic else ""
        self.birth_date = self.parse_date(birth_date)
        self.death_date = self.parse_date(death_date) if death_date else None
        self.gender = gender if gender in ("m", "f") else ""

    def parse_date(self, date_str):
        date_formats = ["%d.%m.%Y", "%d %m %Y", "%d/%m/%Y", "%d-%m-%Y", "%Y-%m-%d"]
        for date_format in date_formats:
            try:
                return datetime.strptime(date_str, date_format).date()
            except ValueError:
                continue
        raise ValueError("Invalid date format!")

    def calculate_age(self):
        end_date = self.death_date if self.death_date else datetime.now().date()
        age = end_date.year - self.birth_date.year
        if (end_date.month, end_date.day) < (self.birth_date.month, self.birth_date.day):
            age -= 1
        return age

    def __str__(self):
        age = self.calculate_age()
        age_str = f"{age} year old." if age == 1 else f"{age} years old."
        gender_str = f"Gender: {'Male.' if self.gender == 'm' else 'Female.'}" if self.gender else ""
        birth_date_str = self.birth_date.strftime("%d.%m.%Y.")
        death_date_str = f"Died: {self.death_date.strftime("%d.%m.%Y.")}" if self.death_date else ""
        return f"{self.first_name:<10} {self.family_name:<10} {self.patronymic:<10} {age_str:<15} {gender_str:<15} Born: {birth_date_str:<10} {death_date_str:<10}"


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


def main():
    db = Database()

    while True:
        print("\nList of options:")
        print("1 - Add a person")
        print("2 - Search for a person")
        print("3 - Save data to file")
        print("4 - Load data from file")
        print("5 - Exit")

        choice = input("Make your choice, please: ")

        if choice == "1":
            first_name = input("First name: ")
            family_name = input("Family name: ")
            patronymic = input("Patronymic: ")
            birth_date = input("Birth date (dd.mm.yyyy): ")
            death_date = input("Death date (dd.mm.yyyy or leave blank if alive): ")
            gender = input("Gender (m/f): ").lower()
            try:
                person = Person(first_name, family_name, patronymic, birth_date, death_date, gender)
                db.add_person(person)
                print("Person added successfully.")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "2":
            query = input("Search by first name, family name, or patronymic: ")
            results = db.search(query)
            if results:
                print("Search results:")
                for person in results:
                    print(person)
            else:
                print("No records found!")

        elif choice == "3":
            filename = input("Enter the filename: ")
            db.save_to_file(filename)
            print("Data saved.")

        elif choice == "4":
            filename = input("Enter the filename: ")
            if not db.load_from_file(filename):
                print("Failed to load data!")
            else:
                print("Data loaded.")

        elif choice == "5":
            print("Have a great day!")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
