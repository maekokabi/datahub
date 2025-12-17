from expense_manager import ExpenseManager
from note_manager import NoteManager
from task_manager import TaskManager

def run_expense_menu(expense_manager):
    while True:
        print("\nEXPENSE MANAGER")
        print("0- Back")
        print("1- Add expense")
        print("2- Delete expense")
        print("3- Delete expense by id")
        print("4- Search")
        print("5- Display all expenses")

        choice = input("\nWhat do you want to do? ")

        if choice == "1":
            id = int(input("Id: "))
            amount = int(input("Amount: "))
            date = input("Date: ")
            category = input("Category: ")
            necessity = int(input("Necessity: "))
            description = input("Description: ")

            expense_manager.add_expense(id, amount, date, category, necessity, description)

        elif choice == "2":
            id = int(input("Id: "))
            amount = int(input("Amount: "))
            date = input("Date: ")
            category = input("Category: ")
            necessity = int(input("Necessity: "))
            description = input("Description: ")

            expense_manager.delete_expense(id, amount, date, category, necessity, description)

        elif choice == "3":
            expense_id = int(input("\nId: "))

            expense_manager.delete_expense_by_id(expense_id)

        elif choice == "4":
            print("1- Search by category")
            print("2- Search by necessity")
            print("3- Search by date")

            search_choice = input("\nHow do you want to search? ")

            if search_choice == "1":
                search_category = input("\nSearch category: ")
                expense_manager.search_by_category(search_category)

            elif search_choice == "2":
                search_necessity = int(input("\nSearch by necessity: "))
                expense_manager.search_by_necessity(search_necessity)
            
            elif search_choice == "3":
                search_date = input("\nSearch by date: ")
                expense_manager.search_by_date(search_date)
        
        elif choice == "5":
            expense_manager.display_all_expenses()

        elif choice == "0":
            break

        else:
            try:
                print("Wrong input. Try again.")
                run_expense_menu()
            except ValueError as e:
                print(f"{e}")

def run_note_menu(note_manager):
    while True:
        print("\nNOTE MANAGER")
        print("0- Back")
        print("1- Add a new note entry")
        print("2- Delete a note entry")
        print("3- Delete a note entry by id")
        print("4- Search")
        print("5- Display all note entries")

        choice = input("\nWhat do you want to do? ")

        if choice == "1":
            id = int(input("\nId: "))
            category = input("Category: ")
            date = input("Date: ")
            topic = input("Topic: ")
            note = input("Note: \n")

            note_manager.add_note(id, category, date, topic, note)

        elif choice == "2":
            id = int(input("\nId: "))
            category = input("Category: ")
            date = input("Date: ")
            topic = input("Topic: ")
            note = input("Note: \n")

            note_manager.delete_note(id, category, date, topic, note)

        elif choice == "3":
            note_id = int(input("\nNote id: "))
            note_manager.delete_note_by_id(note_id)

        elif choice == "4":
            print("\n1- Search by category")
            print("2- Search by date")
            print("3- Search by topic")

            search_choice = input("\nHow do you want to search? ")

            if search_choice == "1":
                search_category = input("\nSearch by category: ")
                note_manager.search_by_category(search_category)

            elif search_choice == "2":
                search_date = input("\nSearch by date: ")
                note_manager.search_by_date(search_date)

            elif search_choice == "3":
                search_topic = input("\nSearch by topic: ")
                note_manager.search_by_topic(search_topic)

        elif choice == "5":
            note_manager.display_all_notes()

        elif choice == "0":
            break

        else:
            try:
                print("Wrong input. Try again.")
                run_note_menu()
            except ValueError as e:
                print(f"{e}")

def run_task_menu(task_manager):
    while True:
        print("\nTASK MANAGER")
        print("0- Back")
        print("1- Add a new task")
        print("2- Delete a task")
        print("3- Delete a task by id")
        print("4- Mark a task done")
        print("5- Mark a task undone")
        print("6- Search")
        print("7- Display all done tasks")
        print("8- Display all undone tasks")
        print("9- Display all tasks")

        choice = input("\nWhat do you want to do? ")

        if choice == "1":
            id = int(input("\nId: "))
            task = input("Task: ")
            description = input("Description: ")
            deadline = input("Deadline: ")
            status = input("Status: ")

            task_manager.add_task(id, task, description, deadline, status)

        elif choice == "2":
            id = int(input("\nId: "))
            task = input("Task: ")
            description = input("Description: ")
            deadline = input("Deadline: ")
            status = input("Status: \n")

            task_manager.delete_task(id, task, description, deadline, status)

        elif choice == "3":
            delete_id = int(input("\nTask id: "))
            task_manager.delete_task_by_id(delete_id)

        elif choice == "4":
            done_id = int(input("\nTask id: "))
            task_manager.mark_task_done(done_id)

        elif choice == "5":
            undone_id = int(input("\nTask id: "))
            task_manager.mark_task_undone(undone_id)

        elif choice == "6":
            print("\n1- Search by task")
            print("2- Search by deadline\n")

            search_choice = input("How do you want to search?")

            if search_choice == "1":
                search_task = input("\nSearch by task: ")
                task_manager.search_by_task(search_task)

            elif search_choice == "2":
                search_deadline = input("\nSearch by deadline: ")
                task_manager.search_by_deadline(search_deadline)

        elif choice == "7":
            task_manager.all_done_tasks()

        elif choice == "8":
            task_manager.all_not_done_tasks()

        elif choice == "9":
            task_manager.display_tasks()

        elif choice == "0":
            break

        else:
            try:
                print("Wrong input. Try again.")
                run_task_menu()
            except ValueError as e:
                print(f"{e}")

def main():
    expense_manager = ExpenseManager()
    note_manager = NoteManager()
    task_manager = TaskManager()

    expense_manager.load_from_file()
    note_manager.load_from_file()
    task_manager.load_from_file()

    while True:
        print("\nDATA HUB")
        print("1. Expenses")
        print("2. Notes")
        print("3. Tasks")
        print("0. Exit")

        choice = input("Where do you want to go? ")

        if choice == "1":
            run_expense_menu(expense_manager)

        elif choice == "2":
            run_note_menu(note_manager)

        elif choice == "3":
            run_task_menu(task_manager)

        elif choice == "0":
            print("Goodbye.")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()


   






        







                
