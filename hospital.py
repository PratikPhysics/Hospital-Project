"""
Hospital Patient Management System
---------------------------------
A simple OOP-based system to manage patients and doctors in a hospital.
Demonstrates: Encapsulation, Inheritance, Abstraction, and Polymorphism.
"""

from abc import ABC, abstractmethod

# --------------------------------------------
# 1. ABSTRACTION: Abstract Base Class (Person)
# --------------------------------------------
class Person(ABC):
    """
    Abstract base class representing a generic person in the hospital.
    Forces all child classes to implement display_info().
    Encapsulates common attributes and a unique ID generator.
    """
    _id_counter = 1000  # Class variable to auto-generate unique IDs

    def __init__(self, name: str, age: int, contact: str):
        self.__id = Person._id_counter  # Private attribute (Encapsulation)
        Person._id_counter += 1

        self.name = name
        self.age = age
        self.__contact = contact  # Private attribute (Encapsulation)

    # ---------- Encapsulation (Getters & Setters) ----------
    def get_id(self) -> int:
        """Get the private ID."""
        return self.__id

    def get_contact(self) -> str:
        """Get the private contact number."""
        return self.__contact

    def set_contact(self, new_contact: str) -> None:
        """Update the private contact number with validation."""
        if new_contact and len(new_contact) >= 10:
            self.__contact = new_contact
        else:
            print("Error: Invalid contact number.")

    # ---------- Abstraction (Abstract Method) ----------
    @abstractmethod
    def display_info(self) -> str:
        """
        Abstract method: Forces every child class to implement their own
        version of how they display their information.
        """
        pass

    def __str__(self):
        return f"ID: {self.__id} | Name: {self.name} | Age: {self.age}"


# --------------------------------------------
# 2. INHERITANCE: Patient Class (inherits Person)
# --------------------------------------------
class Patient(Person):
    """
    Represents a patient with medical history and admission status.
    Inherits all attributes/methods from Person.
    """

    def __init__(self, name: str, age: int, contact: str, ailment: str):
        super().__init__(name, age, contact)  # Call parent constructor
        self.ailment = ailment
        self.__medical_history = []  # Private list (Encapsulation)
        self.__is_admitted = False   # Private status (Encapsulation)
        self.assigned_doctor = None  # Will hold a Doctor object

    # ---------- Encapsulation (Getters & Setters) ----------
    def add_medical_history(self, entry: str) -> None:
        """Add a private medical history entry."""
        if entry:
            self.__medical_history.append(entry)

    def get_medical_history(self) -> list:
        """Get a copy of the private medical history."""
        return self.__medical_history.copy()

    def admit(self) -> None:
        """Admit the patient to the hospital."""
        self.__is_admitted = True
        print(f"Patient {self.name} has been ADMITTED.")

    def discharge(self) -> None:
        """Discharge the patient from the hospital."""
        self.__is_admitted = False
        print(f"Patient {self.name} has been DISCHARGED.")

    def is_admitted(self) -> bool:
        """Check if the patient is currently admitted."""
        return self.__is_admitted

    # ---------- Polymorphism (Overriding abstract method) ----------
    def display_info(self) -> str:
        """Provides a detailed, formatted string specific to a Patient."""
        doctor_name = self.assigned_doctor.name if self.assigned_doctor else "Not Assigned"
        status = "Admitted" if self.__is_admitted else "Discharged"
        return (f"📋 PATIENT | {super().__str__()} | Ailment: {self.ailment} | "
                f"Status: {status} | Doctor: {doctor_name} | "
                f"History Entries: {len(self.__medical_history)}")


# --------------------------------------------
# 3. INHERITANCE: Doctor Class (inherits Person)
# --------------------------------------------
class Doctor(Person):
    """
    Represents a doctor with a specialization and salary.
    Inherits all attributes/methods from Person.
    """

    def __init__(self, name: str, age: int, contact: str, specialization: str):
        super().__init__(name, age, contact)
        self.specialization = specialization
        self.__salary = 0.0  # Private attribute (Encapsulation)
        self.assigned_patients = []  # List of Patient objects

    # ---------- Encapsulation (Getters & Setters) ----------
    def set_salary(self, amount: float) -> None:
        """Set the private salary with validation."""
        if amount >= 0:
            self.__salary = amount
        else:
            print("Error: Salary cannot be negative.")

    def get_salary(self) -> float:
        """Get the private salary."""
        return self.__salary

    def add_patient(self, patient: Patient) -> None:
        """Assign a patient to this doctor."""
        if patient not in self.assigned_patients:
            self.assigned_patients.append(patient)
            patient.assigned_doctor = self  # Link back to doctor

    # ---------- Polymorphism (Overriding abstract method) ----------
    def display_info(self) -> str:
        """Provides a detailed, formatted string specific to a Doctor."""
        return (f"👨‍⚕️ DOCTOR | {super().__str__()} | Specialization: {self.specialization} | "
                f"Patients Assigned: {len(self.assigned_patients)} | "
                f"Salary: ${self.__salary:,.2f}")


# --------------------------------------------
# 4. SYSTEM CONTROLLER (Hospital Class)
# --------------------------------------------
class Hospital:
    """
    Manages the collection of patients and doctors.
    Acts as the central system orchestrating all operations.
    """

    def __init__(self, name: str):
        self.name = name
        self.__patients = {}  # Private dict: patient_id -> Patient object (Encapsulation)
        self.__doctors = {}   # Private dict: doctor_id -> Doctor object (Encapsulation)

    # ---------- Encapsulation (Controlled access to internal lists) ----------
    def add_patient(self, patient: Patient) -> None:
        """Add a patient to the system."""
        self.__patients[patient.get_id()] = patient
        print(f"✅ Patient '{patient.name}' added successfully (ID: {patient.get_id()}).")

    def add_doctor(self, doctor: Doctor) -> None:
        """Add a doctor to the system."""
        self.__doctors[doctor.get_id()] = doctor
        print(f"✅ Doctor '{doctor.name}' added successfully (ID: {doctor.get_id()}).")

    def find_patient(self, patient_id: int) -> Patient:
        """Find a patient by their ID."""
        return self.__patients.get(patient_id)

    def find_doctor(self, doctor_id: int) -> Doctor:
        """Find a doctor by their ID."""
        return self.__doctors.get(doctor_id)

    def assign_doctor_to_patient(self, patient_id: int, doctor_id: int) -> bool:
        """
        Polymorphism in action: We retrieve both objects (which are subclasses of Person)
        and link them together.
        """
        patient = self.find_patient(patient_id)
        doctor = self.find_doctor(doctor_id)

        if not patient:
            print(f"❌ Error: Patient with ID {patient_id} not found.")
            return False
        if not doctor:
            print(f"❌ Error: Doctor with ID {doctor_id} not found.")
            return False

        doctor.add_patient(patient)  # Link doctor -> patient
        patient.assigned_doctor = doctor  # Link patient -> doctor
        print(f"✅ Dr. '{doctor.name}' assigned to patient '{patient.name}'.")
        return True

    # ---------- Polymorphism in action (display_info called on different types) ----------
    def display_all_patients(self) -> None:
        """Display info for all patients. Polymorphism ensures correct format."""
        if not self.__patients:
            print("⚠️ No patients registered in the system.")
            return
        print(f"\n--- PATIENT LIST ({self.name}) ---")
        for patient in self.__patients.values():
            print(patient.display_info())  # Calls Patient's overridden method

    def display_all_doctors(self) -> None:
        """Display info for all doctors. Polymorphism ensures correct format."""
        if not self.__doctors:
            print("⚠️ No doctors registered in the system.")
            return
        print(f"\n--- DOCTOR LIST ({self.name}) ---")
        for doctor in self.__doctors.values():
            print(doctor.display_info())  # Calls Doctor's overridden method


# --------------------------------------------
# 5. MAIN EXECUTION (Interactive Menu)
# --------------------------------------------
def main():
    """
    Entry point for the Hospital Management System.
    Provides a simple CLI menu for users to interact with.
    """
    hospital = Hospital("City General Hospital")
    print("🏥 Welcome to the Hospital Management System!")
    print("=" * 50)

    while True:
        print("\n📌 MAIN MENU:")
        print("1. Add a New Patient")
        print("2. Add a New Doctor")
        print("3. Assign a Doctor to a Patient")
        print("4. Admit/Discharge a Patient")
        print("5. View All Patients")
        print("6. View All Doctors")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            name = input("Enter patient name: ").strip()
            age = int(input("Enter age: ").strip())
            contact = input("Enter contact (10+ digits): ").strip()
            ailment = input("Enter ailment/diagnosis: ").strip()
            patient = Patient(name, age, contact, ailment)
            hospital.add_patient(patient)

        elif choice == "2":
            name = input("Enter doctor name: ").strip()
            age = int(input("Enter age: ").strip())
            contact = input("Enter contact (10+ digits): ").strip()
            specialization = input("Enter specialization (e.g., Cardiology): ").strip()
            doctor = Doctor(name, age, contact, specialization)
            salary = float(input("Enter salary for this doctor: ").strip())
            doctor.set_salary(salary)
            hospital.add_doctor(doctor)

        elif choice == "3":
            hospital.display_all_patients()
            hospital.display_all_doctors()
            try:
                p_id = int(input("Enter Patient ID: ").strip())
                d_id = int(input("Enter Doctor ID: ").strip())
                hospital.assign_doctor_to_patient(p_id, d_id)
            except ValueError:
                print("❌ Invalid ID. Please enter numbers only.")

        elif choice == "4":
            hospital.display_all_patients()
            try:
                p_id = int(input("Enter Patient ID to toggle admission: ").strip())
                patient = hospital.find_patient(p_id)
                if patient:
                    if patient.is_admitted():
                        patient.discharge()
                    else:
                        patient.admit()
                else:
                    print("❌ Patient not found.")
            except ValueError:
                print("❌ Invalid ID.")

        elif choice == "5":
            hospital.display_all_patients()

        elif choice == "6":
            hospital.display_all_doctors()

        elif choice == "7":
            print("👋 Exiting system. Goodbye!")
            break

        else:
            print("❌ Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
