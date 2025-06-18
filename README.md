# Hospital Patient Records Manager (Python CLI CRUD App)

A simple terminal-based application written in Python for managing hospital patient data using CRUD (Create, Read, Update, Delete) functionalities. This tool allows users to interact with patient information in a structured way, mimicking basic operations in a hospital information system.

## 🧩 Features

- 📋 View all patient data in a formatted table
- 🔍 Search for a specific patient using a unique ID
- ➕ Add new patients with validated inputs
- ✏️ Update selected patient fields (name, birthdate, gender, insurance, stages of care, and treatment process.)
- 🗑️ Delete specific patients or bulk-delete those marked as "Completed"
- 📜 View deleted patient history
- ❗ Input validation and user confirmation for critical operations

## 🗃️ Data Fields

Each patient record includes:

- Patient Code (unique identifier)
- Full Name
- Gender (M/F)
- Date of Birth (Day-Month-Year format)
- Insurance Type (BPJS or Non-BPJS)
- Type of Care (Inpatient or Outpatient)
- Treatment Status (Ongoing or Completed)

Data is stored in a list of dictionaries structure within the application runtime.

## 🚀 How to Run

1. Ensure you have Python 3 installed.
2. Run the script in the terminal:
  Hospital Patient Records Manager (Python CLI CRUD Application).py

3. Follow the on-screen numbered menu to navigate:

1: Display patient data

2: Add new patient

3: Edit patient details

4: Delete patient(s)

5: Exit program

## 🧠 Example Use Cases 
Prototyping hospital data flows in a terminal environment.

Beginner-level practice with Python dictionaries, lists, functions, and conditionals.

Demonstrating basic validation, input handling, and menu logic in CLI applications.

✅ Requirements
Python 3.x

## 🧑‍💻 Developer Note
This project was built as a learning and simulation tool, ideal for assignments, tutorials, or demonstrations involving CRUD concepts in Python. It does not persist data beyond the runtime session (no database or file storage used).
