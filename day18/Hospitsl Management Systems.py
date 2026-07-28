# Hospital Management System
# 
# Features:
# 
# Patient
# Doctor
# Appointment
# Billing
# Medical Records
# 
# Use:
# 
# Classes
# Composition
# Encapsulation

class Patient:
    def __init__(self,name,patient_id,age,disease):
        self.name=name
        self.patient_id=patient_id
        self.age=age
        self.disease=disease

    def display(self):
        print("\nPatient Details :")
        print(f"Patient ID :{self.patient_id}")
        print(f"Name       :{self.name}")
        print(f"Age        :{self.age}")
        print(f"Disease    :{self.disease}")

class Doctor:
    def __init__(self,doctor_id,name,specialization):
        self.doctor_id=doctor_id
        self.name=name
        self.specialization=specialization

    def display(self):
        print(f"\nDoctor Details :")
        print(f"Doctor ID      :{self.doctor_id}")
        print(f"Name           :{self.name}")
        print(f"Specialization :{self.specialization}")

class Appointment:
    def __init__(self,patient,doctor,date):
        self.patient=patient
        self.doctor=doctor
        self.date=date

    def display(self):
        print("\nAppointment Details :")
        print(f"Patient :{self.patient.name}")
        print(f"Doctor  :{self.doctor.name}")
        print(f"Date    :{self.date}")

class Billing:
    def __init__(self,patient):
        self.patient=patient
        self.__amount=0

    def generate_bill(self,amount):
        self.__amount=amount

    def display(self):
        print(f"-------------------")
        print(f"Name :{self.patient.name}")
        print(f"Bill :{self.__amount}")

class MedicalRecords:
    def __init__(self,patient,diagnosis,medicines):
        self.patient=patient
        self.diagnosis=diagnosis
        self.medicines=medicines
    
    def display(self):
        print(f"--------------------")
        print(f"Patient   :{self.patient.name}")
        print(f"Diagnosis :{self.diagnosis}")
        print(f"Medicines :{self.medicines}")

class Hospital:
    def __init__(self):
        self.patients=[]
        self.doctors=[]
        self.appointments=[]
        self.bills=[]
        self.records=[]

    def add_patient(self):
        pid=int(input("Enter Padient Id :"))
        name=input("Enter Patient Name :")
        age=int(input("Enter PAtient Age :"))
        disease=input("ENter Disease :")

        patient=Patient(name,pid,age,disease)
        self.patients.append(patient)
        print("Patient Added Successfully.")

    def add_doctor(self):
        did=int(input("Enter Doctor Id :"))
        name=input("Enter Doctor Name :")
        specialization=input("Enter Specialization :")

        doctor=Doctor(did,name,specialization)
        self.doctors.append(doctor)
        print("Doctor Added Successfully.")    

    def show_patients(self):
        if len(self.patients)==0:
            print("No Patients Found.")
            return
        
        print("======Patients Lists======")
        for patient in self.patients:
            patient.display()
            print()

    def show_doctors(self):
        if len(self.doctors)==0:
            print("No Doctors Found.")
            return
        
        print("======Doctors Lists======")
        for doctor in self.doctors:
            doctor.display()
            print()
    
    def book_appointment(self):
        if len(self.doctors)==0 or len(self.patients)==0:
            print("No Doctors Or Patients Found.")-1
            return
        
        print("Patients :")
        for i in range(len(self.patients)):
            print(f"{i+1},{self.patients[i].name}")
        p=int(input("Choose Patient :"))-1

        print("Doctors :")
        for i in range(len(self.doctors)):
            print(f"{i+1},{self.doctors[i].name}")
        d=int(input("Choose Doctor :"))-1
        date=input("Enter Appintment Date :")

        appointment=Appointment(
            self.patients[p],
            self.doctors[d],
            date)
        self.appointments.append(appointment)
        print("Appintment Booked Successfully.")

    def show_appointments(self):

        if len(self.appointments) == 0:
            print("No Appointments.")
            return

        print("\n===== Appointments =====")

        for appointment in self.appointments:
            appointment.display()

    # ---------------- Billing ----------------

    def generate_bill(self):

        if len(self.patients) == 0:
            print("No Patients.")
            return

        for i in range(len(self.patients)):
            print(i + 1, self.patients[i].name)

        choice = int(input("Choose Patient : "))-1

        amount = float(input("Enter Bill Amount : "))

        bill = Billing(self.patients[choice])
        bill.generate_bill(amount)

        self.bills.append(bill)

        print("Bill Generated.")

    def show_bills(self):

        if len(self.bills) == 0:
            print("No Bills.")
            return

        print("\n===== Bills =====")

        for bill in self.bills:
            bill.display()

    # ---------------- Medical Records ----------------

    def add_medical_record(self):

        if len(self.patients) == 0:
            print("No Patients.")
            return

        for i in range(len(self.patients)):
            print(i + 1, self.patients[i].name)

        choice = int(input("Choose Patient : "))-1 

        diagnosis = input("Diagnosis : ")
        medicines = input("Medicines : ")

        record = MedicalRecords(
            self.patients[choice],
            diagnosis,
            medicines
        )

        self.records.append(record)

        print("Medical Record Saved.")

    def show_records(self):

        if len(self.records) == 0:
            print("No Records.")
            return

        print("\n===== Medical Records =====")

        for record in self.records:
            record.display()


hospital = Hospital()

while True:

    print("\n========== Hospital Management ==========")
    print("1. Add Patient")
    print("2. Add Doctor")
    print("3. Show Patients")
    print("4. Show Doctors")
    print("5. Book Appointment")
    print("6. Show Appointments")
    print("7. Generate Bill")
    print("8. Show Bills")
    print("9. Add Medical Record")
    print("10. Show Medical Records")
    print("11. Exit")

    choice = int(input("Enter Choice : "))

    if choice == 1:
        hospital.add_patient()

    elif choice == 2:
        hospital.add_doctor()

    elif choice == 3:
        hospital.show_patients()

    elif choice == 4:
        hospital.show_doctors()

    elif choice == 5:
        hospital.book_appointment()

    elif choice == 6:
        hospital.show_appointments()

    elif choice == 7:
        hospital.generate_bill()

    elif choice == 8:
        hospital.show_bills()

    elif choice == 9:
        hospital.add_medical_record()

    elif choice == 10:
        hospital.show_records()

    elif choice == 11:
        print("Thank You!")
        break

    else:
        print("Invalid Choice.")



