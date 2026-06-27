# 🏥 Hospital Patient Management System

A simple yet robust console-based Hospital Management System built using **Python 3** and core **Object-Oriented Programming (OOP)** principles. 

This project is designed as a practical demonstration of OOP concepts for developers, students, and coding interview preparation. It features auto-generating IDs, encapsulation of sensitive data, and a fully interactive command-line interface.

## 🚀 Features

- **Patient Management:** Add new patients with their ailment, medical history, and admission status.
- **Doctor Management:** Add doctors with their specialization and salary details.
- **Smart Assignments:** Assign a specific doctor to a patient and view the relationship on both ends.
- **Admission Control:** Admit or discharge patients with a single toggle command.
- **Comprehensive Views:** Display neatly formatted lists of all patients and doctors in the system.
- **Auto-Generated IDs:** Every patient and doctor receives a unique ID automatically.

## 🧠 OOP Concepts Demonstrated

This project is heavily commented to showcase the four pillars of OOP in Python:

| Concept | Implementation |
| :--- | :--- |
| **Abstraction** | The `Person` class is an `ABC` (Abstract Base Class) with an abstract `display_info()` method, forcing child classes to implement their own details. |
| **Encapsulation** | Sensitive data like `__salary`, `__contact`, `__medical_history`, and internal patient lists are hidden using double underscores (`__`) and accessed via controlled getters/setters. |
| **Inheritance** | The `Patient` and `Doctor` classes inherit common attributes (`name`, `age`, `id`) and methods from the base `Person` class, reducing code duplication. |
| **Polymorphism** | The `display_info()` method behaves differently for `Patient` and `Doctor` objects. The `Hospital` system treats all subclasses of `Person` uniformly. |

## 🛠️ Requirements

- **Python 3.7** or higher (uses `abc` module, f-strings, and type hints).

## 📥 Installation & Usage

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/hospital-management-system.git
    cd hospital-management-system
