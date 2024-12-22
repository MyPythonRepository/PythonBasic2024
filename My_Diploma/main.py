from database import Database
from person import Person


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
