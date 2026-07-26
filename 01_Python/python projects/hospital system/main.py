from hospital import Hospital
import patient
import doctor
import appointment
import file_manager

# import doctor
# import appointment


print("========= Hospital Management System =========")

def menu():
    print("1. Patient Management")
    print("2. Doctor Management")
    print("3. Appointment Management")
    print("4. Exit")

def main():
    hospital_obj = Hospital()
    while True:
        menu()
        choice = int(input("Enter your choice 1 to 4 :"))
        if choice == 1:
            Hospital.register_patient()
            # name = input("Enter your name : ")
            # age = input("Enter your age : ")
            # gender = input("Enter Gender: ")
            # contact = input("Enter Contact Number: ")
            # address = input("Enter Address: ")
            # blood_group = input("Enter Blood Group: ")
            # disease = input("Enter Disease: ")
            
            # new_patient = patient.Patient(name, age, gender, contact, address, blood_group,disease)
            # manager = file_manager.FileManager()
            # manager.save_patient(new_patient)

        elif choice == 2:
            Hospital.register_doctor()
        elif choice == 3:
            Hospital.book_appointment()
        elif choice == 4:
            print("Thank you for using Hospital Management System.")
            print("Good Bye!")
            break
        else:
            print("Invalid Choice ")


if __name__ == "__main__":
    main()