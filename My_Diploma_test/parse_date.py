from datetime import datetime


class Person:
    def __init__(self, first_name, birth_date):
        self.first_name = first_name
        self.birth_date = self.parse_date(birth_date)

    def parse_date(self, date_str):
        date_formats = ["%d.%m.%Y", "%d %m %Y", "%d/%m/%Y", "%d-%m-%Y", "%Y-%m-%d"]
        for date_format in date_formats:
            try:
                return datetime.strptime(date_str, date_format).date()
            except ValueError:
                continue
        raise ValueError("Invalid date format!")

    def __str__(self):
        return f"Person: {self.first_name}. Birth date: {self.birth_date}"


try:
    person1 = Person("Ana", "25.12.2024")
    person2 = Person("Alex", "25 12 2024")
    person3 = Person("Bob", "25/12/2024")
    person4 = Person("John", "25-12-2024")
    person5 = Person("Mike", "2024-12-25")

    print(person1)
    print(person2)
    print(person3)
    print(person4)
    print(person5)

except ValueError as e:
    print(f"Error: {e}")

try:
    person6 = Person("Anna", "31.02.2004")

    print(person6)

except ValueError as e:
    print(f"\nError: {e}")
