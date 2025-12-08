from datetime import datetime
import json

class ExpenseManager:
    def __init__(self):
        self.expenses = []

    def save_to_file(self, filename="expenses.json"):
        data = {
            "expenses" : [expense.to_dict() for expense in self.expenses]
        }

        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
        print("Data Saved.")

    def load_from_file(self, filename="expenses.json"):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                self.expenses = [Expense.from_dict(expense) for expense in data["expenses"]]
        except FileNotFoundError:
            print("No saved file found.")
        except json.JSONDecodeError:
            print("JSON file is corrupted.")
        except KeyError:
            print("JSON structure missing.")

    def add_expense(self, expense_object):
        if any(e.id == expense_object.id for e in self.expenses):
            print("This id already exists.")
        else:
            try:
                expense_object.validate_all()
                self.expenses.append(expense_object)
                print("Expense added.")
            except ValueError as e:
                print(f"{e}")

    def delete_expense(self, expense_object):
        if not any(e == expense_object for e in self.expenses):
            print("This entry does not exist.")
        else:
            try:
                self.expenses.remove(expense_object)
                print("Expense removed.")
            except ValueError as e:
                print(f"{e}")

    def delete_expense_by_id(self, expense_id):
        if not any(e.id == expense_id for e in self.expenses):
            print("No exisiting entry with this id.")
        else:
            try:
                matched_expense = next((e for e in self.expenses if e.id == expense_id), None)
                self.expenses.remove(matched_expense)
                print("Expense removed.")
            except ValueError as e:
                print(f"{e}")

    def display_all_expenses(self):
        if self.expenses == []:
            print("No expenses entry.")
        else:
            for expense in self.expenses: 
                print(expense)

    def search_by_category(self, category):
        if not any(e.category == category for e in self.expenses):
            print("No exisiting entry for this category.")
        else:
            try:
                print(f"All entries for the category: {category}")
                [print(e) for e in self.expenses if e.category == category]
            except ValueError as e:
                print(f"{e}")

    def search_by_necessity(self, necissity):
        pass

    def search_by_date(self, date):
        pass
        

class Expense:
    def __init__(self, id:int, amount, date, category, necessity:int, description=""):
        self.id = id
        self.amount = amount
        self.date = date
        self.category = category
        self.necessity = necessity
        self.description = description

    def __repr__(self):
        return f"'ID': {self.id}, 'Amount': {self.amount}, 'Date': {self.date}, 'Category': {self.category}, 'Necessity': {self.necessity}, 'Description': {self.description}"
    
    def to_dict(self):
        return {
            "id": self.id,
            "amount": self.amount,
            "date": self.date,
            "category": self.category,
            "necessity": self.necessity,
            "description": self.description
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            data["id"],
            data["amount"],
            data["date"],
            data["category"],
            data["necessity"],
            data["description"]
        )
    
    def validate_all(self):
        errors = []

        for validator in [
            self.validate_id,
            self.validate_amount,
            self.validate_date,
            self.validate_category,
            self.validate_necessity,
            self.validate_description
        ]:
            result = validator()
            if result is not None:
                errors.append(result)
            
        if errors:
            message = " | ".join(errors)
            raise ValueError(f"Invalid expense: {message}")
    
    def validate_id(self):
        if not isinstance(self.id, int):
            return "ID must be a number."
        return None

    def validate_amount(self):
        if not isinstance(self.amount, (int, float)):
            return "Amount must be a number."
        if self.amount <= 0:
            return "Amount must be greater than 0."     
        return None
    
    def validate_date(self):
        try:
            datetime.strptime(self.date, "%Y-%m-%d")
        except ValueError:
            return "Date must be in YYYY-MM-DD format."
        return None

    def validate_category(self):
        if not isinstance(self.category, str) or not self.category.strip():
            return "Category must be a non-empty string."        
        return None

    def validate_necessity(self):
        if  not self.necessity in range(1, 6):
            return "Necessity must be a number in range of 1-5"
        return None

    def validate_description(self):
        if not isinstance(self.description, str):
            return "Description must be a string."        
        return None


        