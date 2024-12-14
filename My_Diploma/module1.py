# Імпорт пакету
# import my_package

# Імпорт модуля з пакету
# from my_package import module1


from datetime import datetime


class Person:
    def __init__(self, first_name, birth_date, family_name = "", patronymic = "", death_date = "", gender = ""):
        self.first_name = first_name
        self.birth_date = birth_date
        self.family_name = family_name
        self.patronymic = patronymic
        self.death_date = death_date
        self.gender = gender

    def analyse_date(self, date_string):
        if not date_string:
            return None
        date_formats = ["%d.%m.Y", "%d %m Y", "%d/%m/Y", "%d-%m-Y"]
        for d_format in date_formats:
            try:
                return datetime.strptime(date_string, d_format).date()
            except ValueError:
                continue
        raise ValueError("Invalid date format")

    def calculate_age(self):
        end_date = self.death_date if self.death_date else datetime.now().date()
        if not self.birth_date:
            return None
        age_in_years = (end_date - self.birth_date).days // 365
        return age_in_years