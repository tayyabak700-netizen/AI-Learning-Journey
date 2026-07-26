class Person:
    def __init__(self, name, age, gender, contact_Number, address):
        self.name = name
        self.age = age
        self.gender = gender
        self.contact_number = contact_Number
        self.address = address

    def display_information(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender : {self.gender}")
        print(f"Contact Number: {self.contact_number}")
        print(f"Address : {self.address}")

    def update_details(self):
        print("--- Update Details ---")
        new_name = input("Enter your new Name which you want to change : ")
        new_age = input("Enter your age which you want to change")
        new_gender = input("Enter your gender which you want to change")
        new_contact_number = input("Enter new Contact which you want to change : ")
        new_address = input("Enter Your new address which you want to change : ")
        if new_name == "":
            self.name = new_name
        if new_age == "":
            self.age = new_age
        if new_gender == "":
            self.gender = new_gender
        if new_contact_number == "":
            self.contact_number = new_contact_number
        if new_address == "":
            self.address = new_address
        print("--- UPDATED SUCCESSFULLY---")
        self.display_information()
    


person = Person("tayyaba", 21, "female", 341, "okara")
person.display_information()


