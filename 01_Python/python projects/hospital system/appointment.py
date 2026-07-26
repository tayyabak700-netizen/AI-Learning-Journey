import random
import string
class Appointment:
    def __init__(self,  patient_id, doctor_id, date, time, status = "booked" ):
        self.appointment_id = self.generate_id()
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.date = date
        self.time = time
        status = status.lower()
        if status in ["active", "booked", "canceled"]:
            self.status = status
        else:
            print("invalid Status")



    def generate_id(self):
        letters = random.choices(string.ascii_uppercase , k=2)
        digits = random.choices(string.digits, k=3)
        appointment_id = letters + digits 
        random.shuffle(appointment_id)
        return "".join(appointment_id)
    

    def display_information(self):
        print("-- Appointment Information --")
        print(f"Appointment ID : {self.appointment_id}")
        print(f"Patient ID : {self.patient_id}")
        print(f"Doctor ID : {self.doctor_id}")
        print(f"Date : {self.date}")
        print(f"Time : {self.time}")
        print(f"Status : {self.status}")


    def update_information(self):
        print("Enter details for update ")
        new_info = {
            "date" : input("Enter new date : "),
            "time" : input("Enter new time : "),
            "status" : input("Enter new status : ")
        }
        
        if new_info['date'] != "":
            self.date = new_info['date']
        if new_info['time'] != "":
            self.time = new_info['time']
        if new_info['status'] != "":
            status = new_info['status'].lower()
            if status in ["active", "booked", "canceled"]:
                self.status = self.status
                self.status = new_info['status']
                
            else:
             print("invalid Status")
        print("--- UPDATED SUCCESSFULLY---")
        self.display_information()

    def to_dict(self):
        return{
            "appointment_id" : self.appointment_id,
            "patient_id"  : self.patient_id,
            "doctor_id" : self.doctor_id,
            "date" : self.date,
            "time" : self.time,
            "status" : self.status
        }
    
doctor = Appointment("AI123", "AI124", 1,2,"booked")
doctor.display_information()
doctor.update_information()