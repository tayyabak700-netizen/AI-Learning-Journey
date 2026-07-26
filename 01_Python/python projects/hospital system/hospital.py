from file_manager import FileManager
import patient
import doctor
import appointment

class Hospital:
    def __init__(self):
        self.file_manager = FileManager()
    
    def register_patient(self):
        name = input("Enter your name : ")
        age = input("Enter your age : ")
        gender = input("Enter Gender: ")
        contact = input("Enter Contact Number: ")
        address = input("Enter Address: ")
        blood_group = input("Enter Blood Group: ")
        disease = input("Enter Disease: ")
            
        new_patient = patient.Patient(name, age, gender, contact, address, blood_group,disease)
        self.manager.save_patient(new_patient)
        print("-- Register Patient Successfully -- ")

    def register_doctor(self):

        name = input("Enter your Name : ")
        age = input("Enter your Age : ")
        gender = input("Enter Gender: ")
        contact = input("Enter Contact Number: ")
        address = input("Enter Address: ")
        specialization = input("Enter Specialization : ")
        experience = input("Enter Experience : ")
        availability = input("Enter Availability : ")
        new_doctor = doctor.Doctor(name, age, gender, contact, address,specialization, experience, availability)
        self.manager.save_doctor(new_doctor)
        print("-- Register Doctor Successfully --")

    def book_appointment(self):
        print("For booking appoitment please Enter the required data ")
        patient_id = input("Enter Doctor ID: ")
        doctor_id = input("Enter  ID: ")
        patient = self.file_manager.load_patients()
        doctor = self.file_manager.load_doctors()
        for i in patient:
            if patient_id == i[patient_id]:
                disease = i["disease"]
        for i in doctor:
            if doctor_id == i[doctor_id]:
                specialization = i["specialization"]

        if disease == specialization:
            doctor.display_information()
                



    # def search_patient(self):
    #     key_patient_id = input("Please your patient Id : ")
    #     if key_patient_id == self.patient_id:
    #         self.display_patient()
    #     else:
    #         print("Invalid ID ! ")
    

