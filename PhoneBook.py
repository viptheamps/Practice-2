class PhoneBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self):
        name = input("Enter contact name: ")
        number = input("Enter phone number: ")
        self.contacts[name] = number
        print("Contact added successfully.")

    def look_up_contact(self):
        name = input("Enter contact name: ")
        if name in self.contacts:
            print(name + "'s phone number is", self.contacts[name] + ".")
        else:
            print("Contact not found.")

    def delete_contact(self):
        name = input("Enter contact name: ")
        if name in self.contacts:
            del self.contacts[name]
            print("Contact deleted successfully.")
        else:
            print("Contact not found.")

    def display_menu(self):
        print("Phone Book:")
        print("1. Add contact")
        print("2. Look up contact")
        print("3. Delete contact")
        print("4. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")
            if choice == '1':
                self.add_contact()
            elif choice == '2':
                self.look_up_contact()
            elif choice == '3':
                self.delete_contact()
            elif choice == '4':
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Please enter a number from 1 to 4.")

phone_book = PhoneBook()
phone_book.run()
