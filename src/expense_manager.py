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

    def load_from_file(self, filename="expenses.json"):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                self.expenses = [Expense.from_dict(expense) for expense in data["expenses"]]
        except FileNotFoundError:
            raise ValueError("No saved file found.")
        except json.JSONDecodeError:
            raise ValueError("JSON file is corrupted.")
        except KeyError:
            raise ValueError("JSON structure missing.")

    def add_expense(self, id, amount, date, category, necessity, description=""):
        expense_object = Expense(id, amount, date, category, necessity, description)
        if any(e.id == expense_object.id for e in self.expenses):
            raise ValueError("This id already exists.")
        else:
            expense_object.validate_all()
            self.expenses.append(expense_object)
            self.save_to_file()       
            
    def delete_expense_by_id(self, expense_id):
        if not any(e.id == expense_id for e in self.expenses):
            raise ValueError("No exisiting entry with this id.")
        else:
            matched_expense = next((e for e in self.expenses if e.id == expense_id), None)
            self.expenses.remove(matched_expense)
            self.save_to_file()

    def display_all_expenses(self):
        if not self.expenses: 
            raise ValueError("No expenses entry.")
        return self.expenses
    
    def search_by_attribute(self, attr_name, value):
        results = [e for e in self.expenses if getattr(e, attr_name) == value]
        if not results:
            raise ValueError(f"No entries found for {attr_name} = {value}")
        return results

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


        