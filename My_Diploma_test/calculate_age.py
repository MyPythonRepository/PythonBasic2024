from datetime import datetime


class Person:
    def __init__(self, first_name, birth_date, death_date=None):
        self.first_name = first_name
        self.birth_date = datetime.strptime(birth_date, "%d.%m.%Y").date()
        self.death_date = datetime.strptime(death_date, "%d.%m.%Y").date() if death_date else None

    def calculate_age(self):
        end_date = self.death_date if self.death_date else datetime.now().date()
        age = end_date.year - self.birth_date.year
        if (end_date.month, end_date.day) < (self.birth_date.month, self.birth_date.day):
            age -= 1
        return age


person1 = Person("Alex", "20.05.1990")  # Alive person
person2 = Person("Bob", "15.03.1975", "10.02.2020")  # Dead person
person3 = Person("Ana", "29.12.2000")  # Alive person with date of birth later this year

print(f"{person1.first_name}'s age: {person1.calculate_age()} years old.")
print(f"{person2.first_name}'s age: {person2.calculate_age()} years old.")
print(f"{person3.first_name}'s age: {person3.calculate_age()} years old.")
