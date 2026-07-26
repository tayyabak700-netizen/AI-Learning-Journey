import json
from pathlib import Path

class FileManager:
    def __init__(self):
        base_path = Path(__file__).parent
        self.data_folder = base_path/"data"
        self.patient_file = self.data_folder/"patients.json"
        self.doctor_file = self.data_folder/"doctors.json"
        self.appointment_file = self.data_folder/"appointments.json"
        if not self.data_folder.exists():
            self.data_folder.mkdir()
        

    def save_patient(self, patient):
        try:
            patient_data = patient.to_dict()
            file_path = self.patient_file
            if file_path.exists():
                with open(file_path, 'r')as file:
                    patients = json.load(file)
                

            else:
                patients = []

            patients.append(patient_data)
            with open(file_path, 'w') as file:
                    json.dump(patients,file, indent=4)
        except Exception as err:
            print(f"there is an error {err}")


    def load_patient(self):
        file_path = self.patient_file
        if file_path.exists():
            with open(file_path, 'r') as file:
                patient = json.load(file)
        else:
            patient = []

        return patient     
            
    def save_doctor(self, doctors):
        try: 
            doctor_data = doctors.to_dict()
            file_path = self.doctor_file
            if file_path.exists():
                with open(file_path, 'r')as file:
                    doctors = json.load(file)
            else:
                doctors = []
            
            doctors.append(doctor_data)
            with open(file_path, 'w')as file:
                json.dump(doctors, file,indent = 4)

        except Exception as err:
            print(f"there is an error {err}") 


    def load_doctor(self):
        file_path = self.doctor_file
        if file_path.exists():
            with open(file_path, 'r')as file:
                doctor = json.load(file)
        else:
            doctor = []
        return doctor
        
    def save_appointment(self, appointments):
        try:
            appointment_data = appointments.to_dict()
            file_path = self.appointment_file
            if file_path.exists():
                with open(file_path, 'r')as file:
                    appointments = json.load(file)
            else:
                appointments = []

            appointments.append(appointment_data)
            with open(file_path, 'w')as file:
                json.dump(appointments, file, indent = 4)

        except Exception as err:
            print(f"there is an error : {err}")

    def load_appointments(self):
        file_path = self.appointment_file
        if file_path.exists():
            with open(file_path, 'r')as file:
                appointments = json.load(file)
        else:
            appointments = []
        return appointments