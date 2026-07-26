import person
import random
import string

class Doctor(person.Person):
    def __init__(self, name, age, gender, contact_Number, address, specialization, experience, availability):
        super().__init__(name, age, gender, contact_Number, address)
        self.doctor_id = self.generate_id()
        self.specialization = specialization
        self.experience = experience
        self.availability = availability
        self.doctor_id = self.generate_id()
        

    def generate_id(self):
        letters = random.choices(string.ascii_uppercase, k = 2)
        num = random.choices(string.digits, k = 3)
        doctor_id = letters + num
        random.shuffle(doctor_id)
        return "".join(doctor_id)
       

        
    def dispaly_information(self):
        print(f"Doctor ID : {self.doctor_id}")  
        print(f"Doctor Name : {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender : {self.gender}")
        print(f"Contact Number: {self.contact_number}")
        print(f"Address : {self.address}")
        print(f"Specialization : {self.specialization}")
        print(f"Experience : {self.experience}")
        print(f"Availability : {self.availability}")
    

    def update_doctor(self):
        print("--Enter record for update record --")
        new_data = {
                "name" : input("Enter the name : "),
                "age" : int(input("Enter the new age : ")),
                "gender" : input("Enter the new gender : "),
                "address" : input("Enter the new Address  : "),
                "contact_number": int(input("Enter the new contact number : ")),
                "Specialization" : input("Enetr your new Specialization : "),
                "experience" : input("Enter your new Experience")

            }
        if new_data['name'] != "":
            self.name = new_data['name']
        if new_data['age'] != "":
            self.age = new_data['age']
        if new_data['gender'] != "":
            self.gender = new_data['gender']
        if new_data['address'] != "":
            self.address = new_data['address']
        if new_data['contact_number'] != "":
            self.contact_number = new_data['contact_number']
        if new_data['Specialization'] != "":
            self.specialization = new_data['Specialization']
        if new_data['experience'] != "":
            self.experience = new_data['experience']

        print("--- UPDATED SUCCESSFULLY---")
        self.dispaly_information()
        



    def to_dict(self):
        return{
            "doctor_id" : self.doctor_id,
            "name" : self.name,
            "age" : self.age,
            "gender" : self.gender,
            "address": self.address,
            "contact_number" : self.contact_number,
            "specialization" : self.specialization,
            "experience" : self.experience

        }


doctor2 = Doctor("tayyaba", 21, "female", 982,"okara", "heart", 5, "yes")
doctor2.dispaly_information()
# doctor2.update_doctor()

