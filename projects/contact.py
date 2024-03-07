class Contact:
    def __init__(self, name, number, email):
        self.name = name
        self.number = number
        self.email = email

    def display_details(self):
        print("Name: ", self.name)
        print("Number: ", self.number)
        print("Email: ", self.email)
        print()

    @classmethod
    def add_contacts(cls, contact_list):
        name = input("Enter name: ")
        number = input("Enter number: ")
        email = input("Enter number: ")
        contact_list.append(cls(name, number, email))
        print("Contact added successfully")


def main():
    contacts = []

    while True:
        print("Pick 1, to add a contact")
        print("Pick 2, to show contact detail")
        print("Pick 3, to exit")

        choice = int(input("Enter one option from the above: "))

        if choice == 1:
            Contact.add_contacts(contacts)
        elif choice == 2:
            print("Printing contacts")
            if contacts:
                for contact in contacts:
                    contact.display_details()
            else:
                print("No contact details saved")

        elif choice == 3:
            print("Exiting...")
            break

        else:
            print("Invalide Choice, try again")


if __name__ == "__main__":

    main()
