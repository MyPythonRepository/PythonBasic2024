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
