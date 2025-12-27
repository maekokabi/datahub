# **Lattice**

> A personal data management system integrating **Expenses, Notes, and Tasks** with full CRUD operations. Designed for modularity and future upgrades with APIs, frameworks, and databases.

---

## **Table of Contents**

1. [Project Overview](#project-overview)  
2. [Features](#features)  
3. [Installation](#installation)  
4. [Usage](#usage)  
5. [Project Structure](#project-structure)  
6. [Future Improvements](#future-improvements)  
7. [Technologies](#technologies)  
8. [Contributing](#contributing)  
9. [License](#license)  

---

## **Project Overview**

Lattice is a **personal data manager** that allows users to:

- Track and manage **expenses** with categories, amounts, dates, and priorities  
- Store **notes** organized by topics, categories, and dates  
- Manage **tasks**, including deadlines and completion status  

All data is stored to ensure **persistence across sessions**. The project is built with a **modular architecture**.

---

## **Features**

### **Expense Manager**
- Add, delete, and search expenses  
- Validate inputs and prevent duplicates  
- Automatic saving and loading   

### **Note Manager**
- Add, delete, and search notes  
- Organize by topic, date, and category  
- Persistent storage across sessions  

### **Task Manager**
- Add, delete, search, and manage tasks  
- Mark tasks as done or undone  
- Filter tasks by completion status  
- Automatic saving and loading  

### **Architecture**
- **Managers** handle all business logic  
- **main.py** handles input/output  
- Fully modular, easy to extend for APIs, databases, or GUIs  

---

## Installation

1. Clone the repository:

git clone https://github.com/maekokabi/lattice.git
cd datahub/src

2. Ensure Python 3.10+ is installed.

3. Run the program:

python main.py

---

## Usage

1. Launch the program with `python main.py`
2. Select a manager: Expenses, Notes, or Tasks
3. Follow the on-screen menu to add, delete, search, or display entries
4. All data changes are automatically saved 

---

## Project Structure

lattice/
 └── src/
      ├── main.py          # CLI interface
      ├── expense_manager.py
      ├── note_manager.py
      ├── task_manager.py

---

## Future Improvements

- Implement a RESTful API using Flask or FastAPI
- Switch storage to SQLite/PostgreSQL for real-world persistence
- Build a web or mobile frontend
- Add unit and integration tests for all modules
- Implement authentication and multi-user support
- Add real-time data validation and analytics dashboards

---

## Technologies

- Python 3.10+
- JSON for persistent storage
- Object-Oriented Programming (classes, modularity)
- Command Line Interface (CLI)

---

## Contributing

1. Fork the repository
2. Create a new branch:

git checkout -b feature-name

3. Commit your changes:

git commit -m "Add new feature"

4. Push to the branch:

git push origin feature-name

5. Create a Pull Request

---

## License

This project is MIT licensed.



