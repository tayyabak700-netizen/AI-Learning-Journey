# import hospital
import person
import random
import string


class Patient(person.Person):
    def __init__(self , name, age, gender, contact_Number, address, blood_group, disease):
        super().__init__(name, age, gender, contact_Number, address)
        self.patient_id = self.generate_patient_id()
        self.blood_group = blood_group
        self.disease = disease

        
    def generate_patient_id(self):
        letters = random.choices(string.ascii_uppercase, k=2)
        digits = random.choices(string.digits, k = 4)
        patient_id = letters + digits
        random.shuffle(patient_id)
        return "".join(patient_id)
        # print("Please Note Down Your patient ID")
        # print(f"Patient id : {patient_id}")



 
    def display_information(self):
        print(f"Patient ID : {self.patient_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender : {self.gender}")
        print(f"Contact Number: {self.contact_number}")
        print(f"Address : {self.address}")
        print(f"Blood Group : {self.blood_group}")
        print(f"Disease : {self.disease}")


    def update_information(self):
            print("Please enter the record which you want to update")
            new_data = {
                "name" : input("Enter the name : "),
                "address" : input("Enter the new Address  : "),
                "age" : (input("Enter the new age : ")),
                "gender" : input("Enter the new gender : "),
                "contact_number": (input("Enter the new_contact_number : ")),
                "blood_group" : input("Enter your blood group to update : "),
                "disease": input("Enter new Disease : ")
            }

            if new_data["name"] != "":
                self.name  = new_data['name']
            if new_data["age"] != "":
                self.age = int(new_data['age'])
            if new_data["gender"] != "":
                self.gender  = new_data['gender'] 
            if new_data["contact_number"] != "":
                self.contact_number = int(new_data['contact_number'])
            if new_data["address"] != "":
                self.address  = new_data['address']
            if new_data["blood_group"] != "":
                self.blood_group  = new_data['blood_group']
            if new_data["disease"] != "":
                 self.disease = new_data["disease"]
            
            print("--- UPDATED SUCCESSFULLY---")
            self.display_information()



    def to_dict(self):
        return{
            "patient_id" : self.patient_id,
            "name" : self.name, 
            "age" : self.age,
            "gender" : self.gender,
            "contact_number" : self.contact_number,
            "address": self.address, 
            "blood_group" : self.blood_group, 
            "disease" : self.disease
        }
    

# patient = Patient("tayyaba", 22, "female", 123456789, "Sahiwal", "B+", "flue")
# patient.to_dict()
# patient.display_information()
# patient.update_information()

