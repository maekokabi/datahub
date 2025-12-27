from expense_manager import ExpenseManager
from note_manager import NoteManager
from task_manager import TaskManager

def handle_action(func, *args):
    try:
        return func(*args)
    except ValueError as e:
        print(e)
        return None

def run_expense_menu(expense_manager):
    while True:
        print("\nEXPENSE MANAGER")
        print("0- Back")
        print("1- Add expense")
        print("2- Delete expense by id")
        print("3- Search")
        print("4- Display all expenses")

        choice = input("\nWhat do you want to do? ")

        if choice == "1":
            id = int(input("Id: "))
            amount = int(input("Amount: "))
            date = input("Date: ")
            category = input("Category: ")
            necessity = int(input("Necessity: "))
            description = input("Description: ")
            
            handle_action(expense_manager.add_expense, id, amount, date, category, necessity, description)

        elif choice == "2":
            expense_id = int(input("\nId: "))
            
            handle_action(expense_manager.delete_expense_by_id, expense_id)

        elif choice == "3":
            print("1- Search by category")
            print("2- Search by necessity")
            print("3- Search by date")

            search_choice = input("\nHow do you want to search? ")

            if search_choice == "1":
                search_category = input("\nSearch category: ")
                print(f"All entries for the category: {search_category}")
                category_expenses = handle_action(expense_manager.search_by_attribute, "category", search_category)
                if category_expenses:
                    for e in category_expenses:
                        print(e)

            elif search_choice == "2":
                search_necessity = int(input("\nSearch by necessity: "))
                print(f"All entries for this necissity: {search_necessity}")
                necessity_expenses = handle_action(expense_manager.search_by_attribute, "necessity", search_necessity)
                if necessity_expenses:
                    for e in necessity_expenses:
                       print(e)
            
            elif search_choice == "3":
                search_date = input("\nSearch by date: ")
                print(f"All entries for the date: {search_date}")
                date_expenses = handle_action(expense_manager.search_by_attribute, "date", search_date)
                if date_expenses:
                    for e in date_expenses:
                        print(e)
      
        elif choice == "4":
                expenses = handle_action(expense_manager.display_all_expenses)
                if expenses:
                    for e in expenses:
                        print(e)

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
        print("2- Delete a note entry by id")
        print("3- Search")
        print("4- Display all note entries")

        choice = input("\nWhat do you want to do? ")

        if choice == "1":
            id = int(input("\nId: "))
            category = input("Category: ")
            date = input("Date: ")
            topic = input("Topic: ")
            note = input("Note: \n")

            handle_action(note_manager.add_note, id, category, date, topic, note)

        elif choice == "2":
            note_id = int(input("\nNote id: "))
            handle_action(note_manager.delete_note_by_id, note_id)

        elif choice == "3":
            print("\n1- Search by category")
            print("2- Search by date")
            print("3- Search by topic")

            search_choice = input("\nHow do you want to search? ")

            if search_choice == "1":
                search_category = input("\nSearch by category: ")
                category_notes = handle_action(note_manager.search_by_attribute, "category", search_category)
                if category_notes:
                    for n in category_notes:
                        print(n)

            elif search_choice == "2":
                search_date = input("\nSearch by date: ")
                date_notes = handle_action(note_manager.search_by_attribute, "date", search_date)
                if date_notes:
                    for n in date_notes:
                        print(n)

            elif search_choice == "3":
                search_topic = input("\nSearch by topic: ")
                topic_notes = handle_action(note_manager.search_by_attribute, "topic", search_topic)
                if topic_notes:
                    for n in topic_notes:
                        print(n)

        elif choice == "4":
            notes = handle_action(note_manager.display_all_notes)
            if notes:
                for n in notes:
                    print(n)

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
        print("2- Delete a task by id")
        print("3- Mark a task done")
        print("4- Mark a task undone")
        print("5- Search")
        print("6- Display all done tasks")
        print("7- Display all undone tasks")
        print("8- Display all tasks")

        choice = input("\nWhat do you want to do? ")

        if choice == "1":
            id = int(input("\nId: "))
            task = input("Task: ")
            description = input("Description: ")
            deadline = input("Deadline: ")
            status = input("Status: ")

            handle_action(task_manager.add_task, id, task, description, deadline, status)

        elif choice == "2":
            delete_id = int(input("\nTask id: "))
            handle_action(task_manager.delete_task_by_id, delete_id)

        elif choice == "3":
            done_id = int(input("\nTask id: "))
            handle_action(task_manager.mark_task_done, done_id)

        elif choice == "4":
            undone_id = int(input("\nTask id: "))
            handle_action(task_manager.mark_task_undone, undone_id)

        elif choice == "5":
            print("\n1- Search by task")
            print("2- Search by deadline\n")

            search_choice = input("How do you want to search?")

            if search_choice == "1":
                search_task = input("\nSearch by task: ")
                handle_action(task_manager.search_by_attribute, "task", search_task)

            elif search_choice == "2":
                search_deadline = input("\nSearch by deadline: ")
                handle_action(task_manager.search_by_attribute, "deadline", search_deadline)

        elif choice == "6":
            done_tasks = handle_action(task_manager.all_done_tasks)
            if done_tasks:
                for t in done_tasks:
                    print(t)

        elif choice == "7":
            undone_tasks = handle_action(task_manager.all_not_done_tasks)
            if undone_tasks:
                for t in undone_tasks:
                    print(t)

        elif choice == "8":
            tasks = handle_action(task_manager.display_tasks)
            if tasks:
                for t in tasks:
                    print(t)

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


   






        







                
